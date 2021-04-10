from collections import OrderedDict
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django import forms
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, FormView

from accounts.sms import AccountSMS

from .forms import LoginForm, InviteForm
from .models import Account


class LoginView(BaseLoginView):
    """The user can log in to the application."""

    template_name = "accounts/login.html"
    authentication_form = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "login"
        return context
    

@login_required
def ProfileView(request):
    """
        The user can see information about their profile when
        the user logs in.
    """

    context = { "account": request.user }
    return render(request, "accounts/profile.html", context)


class CreateAccountView(CreateView):
    """
        A new user can create a new account.

        This can happen from two paths: 
        - accounts/create/
            - normal account signup 

        - accounts/create/<invite_number>/
            - Invited user 
            - Created with first friend as the inviter.
    """

    model = Account
    template_name = "accounts/create_account.html"
    fields = ["username", "phone", "password"]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['password'].widget = forms.PasswordInput()

        invite_number = self.request.resolver_match.kwargs.pop('invite_number', False)
        if invite_number: 
            form.fields['invite_number'] = forms.CharField(widget=forms.HiddenInput(), initial=invite_number)
            form.fields['invite_number'].label = ''
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "create_account"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        post = OrderedDict()
        post.update(self.request.POST)

        # Check for invite_number.
        invite_number = post.pop('invite_number', False)

        # Add them as the first friend if so.
        if invite_number:
            inviter = Account.objects.get(invite_number=invite_number)
            invited = Account.objects.get(email=post['email'])
            inviter.add_friend(invited)

        return response


class ConfirmAccount(TemplateView):

    template_name = "accounts/profile.html"

    def dispatch(self, request, *args, **kwargs):
        confirmation_number = kwargs["confirmation_number"]
        account = Account.objects.get(confirmation_number=confirmation_number)

        if account.is_confirmed():
            account.confirmed_at = datetime.now() 
            account.save()
            messages.success(request, "Your account is confirmed. Please log in to continue.")

        else: 
            messages.info(request, "It looks like this account has already been confirmed. Log in to continue")


        return redirect(reverse_lazy("profile"))


class ConfirmPhone(TemplateView):

    template_name = "accounts/profile.html"

    def dispatch(self, request, *args, **kwargs):
        confirmation_number = kwargs["confirmation_number"]
        account = Account.objects.get(phone_confirmation_number=confirmation_number)

        if account.is_confirmed():
            account.confirm_phone_number()
            messages.success(request, "Your account is confirmed. Please log in to continue.")

        else: 
            messages.info(request, "It looks like this account has already been confirmed. Log in to continue")


        return redirect(reverse_lazy("profile"))


class InviteUser(LoginRequiredMixin, FormView):

    form_class = InviteForm
    template_name = 'accounts/invite.html'
    success_url = '/'

    def form_valid(self, form):
        AccountSMS().invite_friend(self.request.user, form.cleaned_data['phone_number'])
        return super().form_valid(form)