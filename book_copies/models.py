from django.db import models

from accounts.models import Account
from books.models import Book
from logs.models import Log


# Create your models here.
class BookCopy(models.Model):
    book = models.ForeignKey("books.Book", on_delete=models.PROTECT)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="owned_books")
    borrower = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True, related_name="borrowed_books")
 
    def __str__(self):
        return f"{owners}'s copy of {book}"

    def lend_to(self, borrower):
        self.borrower = borrower
        self.save()

    def return_to_owner(self):
        self.borrower = None
        self.save()

    def mark_available(self, save=False):
        self.available = True

        if save:
            self.save()
        
    def mark_unavailable(self, save=False):
        self.available = False

        if save:
            self.save()
    


    def save(self, *args, **kwargs):
        created = False if self.pk else True
        super(BookCopy, self).save(*args, **kwargs)
        if created:
            Log.objects.create(book_copy=self)

        return self

    
