from django.db import models

# Create your models here.
class BookRequest(models.Model):
    STATUS_CHOICES(
        ('n', 'New'),
        ('a', 'Accepted'),
        ('r', 'Rejected'),
        ('i', 'In Progress'),
        ('r', 'Returned'),
        ('c', 'Complete'),
        ('o', 'Overdue'),
    )
     
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    book_instance = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Account, on_delete=models.CASCADE)
    original_due_date = models.DateField()
    due_date = models.DateField() 

    def accept_request(self, request):
        if request.user != book_instance.owner: 
            raise Exception("Only the owner of the book may except the request.")

        self.status = 'a'
        self.save()

    def reject_request(self, request): 
        if request.user != book_instance.owner: 
            raise Exception("Only the owner of the book may except the request.")

        self.status = 'r'
        self.save()

    def begin_checkout(self): 
        if self.status != 'a':
            raise Exception("This book is not eligible for checkout")

        self.book_instance.lend_to(self.borrower)

        self.status = 'i'
        self.save()

    def return_book(self): 
        self.book.return_to_owner()

        self.status = 'r'
        self.save()