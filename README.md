# books
A decentralized library for people who read paper books. 


## Design
**Terminology** 

[Google Docs](https://docs.google.com/document/d/1ssaj2CkgFQaVrCOrfS8u3M1pvwVOmoWc0Q1YL0BjzgE/edit?usp=sharing)


**User Journey Maps**

[Miro Board](https://miro.com/app/board/o9J_lMm2Kd8=/)


## Running the app

```
python manage.py runserver
```

## Initial configuration 

Install the packages.

```
pip install -r requirements.txt
```

run the migrations
```
python manage.py migrate
```

**SMS**
These environment variables are required to configure the SMS client for text message notifications. 

```
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=
```

Ask Mav if you need them as they are currently associated with a personal account. 

## Common Patterns

**SMS**
```python
from app.sms import SMS

# As a one off message
sms = SMS()
sms.send('<TO_PHONE_NUMBER>', '<MESSAGE>')


# Extending the client for a particular app
class AccountSMS(SMS):
    def send_book_return_reminder(account):
        message = "This is my message for this text" 
        self.send(account.phone_number, message)

sms = AccountSMS():
account = Account.objects.get(email="jeffers@gmail.com")
sms.send_book_return_reminder(account)
```