from django.db import models

from book_requests.models import BookRequest 

class BookCopyManager(models.Manager):
    def on_shelf(self, account):
        return self.filter(
            owner = account, 
            available = True
        )

    def borrowed_by(self, account):
        return self.filter(
            borrower = account,
        )