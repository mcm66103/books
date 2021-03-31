from django.db import models

from accounts.models import Account


class Book(models.Model): 
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="owned_books")
    borrower = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True, related_name="borrowed_books")
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def lend_to(self, borrower):
        self.borrower = borrower
        self.save()

    def return_to_owner(self):
        self.borrower = None
        self.save()
