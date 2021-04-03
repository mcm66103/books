from django.conf import settings
from django.urls import reverse_lazy

class URLHelper():
    def __init__(self): 
        self.base_url = settings.BASE_URL

    def phone_confirmation_url(self, account):
        path = reverse_lazy('confirm_phone', kwargs={"confirmation_number": account.phone_confirmation_number})
        return self.preprend_base_url(path)
    
    def preprend_base_url(self, path): 
        return self.base_url + str(path)