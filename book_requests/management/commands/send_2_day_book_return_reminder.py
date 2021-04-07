import datetime

from django.core.management.base import BaseCommand, CommandError

from book_requests.models import BookRequest
from book_requests.sms import BookRequestSMS


class Command(BaseCommand):
    help = "Sends a 2 day sms reminder on all in progress books."

    def handle(self, *args, **kwargs):
        today = datetime.date.today()

        book_requests = BookRequest.objects.all()
        for book_request in book_requests:
            if book_request.days_until_due() and book_request.days_until_due() < 2:
                self.stdout.write(self.style.SUCCESS(
                    f"notifying borrower {book_request.borrower.id} that "\
                    f"book copy {book_request.book_copy.id} is "\
                    f"due in {book_request.days_until_due()} days"\
                ))

                BookRequestSMS().send_upcoming_due_date_reminder_sms(book_request)

        self.stdout.write(self.style.SUCCESS("Successfully printed all Book titles"))
        
        return