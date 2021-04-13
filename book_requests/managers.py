from django.db import models

class BookRequestManager(models.Manager):
    def lifetime_shares(self, account):
        all_book_shares = self.all_book_shares_by_account(account)
        qualified_book_requests = all_book_shares.filter(status__in =['a', 'i', 'r', 'c','o'])
        return qualified_book_requests

    def all_book_shares_by_account(self, account):
        return self.filter(book_copy__owner=account)