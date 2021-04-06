from django.shortcuts import render


def home(request):
    return render(request, 'app/home.html')

def blog_list(request):
    pass