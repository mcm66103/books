from app.sms import SMS

class BookRequestSMS(SMS):
    @classmethod
    def send_upcoming_due_date_reminder_sms(self, book_request):
        self.send(
            to = book_request.borrower.phone,
            body =  f"Please make plans to return your copy of { book_request.book_copy.book.title } "\
                    f"in { book_request.days_until_due() } days."
        )