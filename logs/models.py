from django.db import models

from accounts.models import Account

# Create your models here.
class Log(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)


class LogEntry(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True, related_name="log_entries")
    entry = models.TextField()