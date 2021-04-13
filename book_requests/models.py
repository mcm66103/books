import datetime

from django.db import models

from accounts.models import Account

from .managers import BookRequestManager


# Create your models here.
class BookRequest(models.Model):
    STATUS_CHOICES = (
        ('n', 'New'),
        ('a', 'Accepted'),
        ('r', 'Rejected'),
        ('i', 'In Progress'),
        ('r', 'Returned'),
        ('c', 'Complete'),
        ('o', 'Overdue'),
    )
     
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    book_copy = models.ForeignKey('book_copies.BookCopy', on_delete=models.CASCADE)
    borrower = models.ForeignKey(Account, on_delete=models.CASCADE)
    checkout_date = models.DateField(blank=True, null=True)
    original_due_date = models.DateField()
    due_date = models.DateField()

    objects = BookRequestManager()

    def accept_request(self, account):
        if account != self.book_copy.owner:
            raise Exception("Only the owner of the book may except the request.")

        self.status = 'a'
        self.save()

        self.book_copy.mark_unavailable()

    def reject_request(self, account): 
        if account != self.book_copy.owner: 
            raise Exception("Only the owner of the book may except the request.")

        self.status = 'r'
        self.save()

    def begin_checkout(self): 
        if self.status != 'a':
            raise Exception("This book is not eligible for checkout")

        self.book_copy.lend_to(self.borrower)

        self.status = 'i'
        self.save()

    def return_book(self): 
        self.book.return_to_owner()

        self.status = 'r'
        self.save()

        self.book_copy.mark_available()

    def days_until_due(self):
        '''
        Returns an integer
            - number of days until the book is due

        OR

        Retruns False
            - When the book has a negative number of days until due.

        Do not use this method to build logic concerning overdue books.
        This method is only for when the number of days until due makes 
        sense.
        '''
        timedelta = self.due_date - datetime.date.today()
        days_remaining = timedelta.days if 0 <= timedelta.days else False
        return days_remaining

    @property
    def checkout_length(self):
        return  (self.due_date - self.checkout_date).days
    
    @property
    def percent_complete(self):
        return 100 - (self.checkout_length - self.days_until_due) / self.checkout_length * 100
