# books
A decentralized library for people who read paper books. 


## Design
**Terminology** 

[Google Docs](https://docs.google.com/document/d/1ssaj2CkgFQaVrCOrfS8u3M1pvwVOmoWc0Q1YL0BjzgE/edit?usp=sharing)


**User Journey Maps**

[Miro Board](https://miro.com/app/board/o9J_lMm2Kd8=/)


**Wireframes**

[figma prototype](https://www.figma.com/proto/Bb3BoGAGiTLHifvJ6aCRhd/BookShare?node-id=105%3A129&view[…]790%2C0.5877559185028076&scaling=scale-down&page-id=102%3A5630)

[figma project file](https://www.figma.com/file/Bb3BoGAGiTLHifvJ6aCRhd/BookShare?node-id=102%3A5630)


## Running the app

```
python manage.py runserver
```


## Updating sass files
This command monitors the `scss` folder for changes and compiles it to css.

```
python manage.py sass app/static/app/scss/ app/static/app/css/ --watch
```


## Running the tests
```
python manage.py test
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
TEST_PHONE=                         # Receives SMS during tests.
```

Ask Mav if you need them as they are currently associated with a personal account. 

**Environment Variables**
```
ENV=development                     # production, development, TODO: staging
BASE_URL=http://127.0.0.1:8000      # You do not want a trailing slash
SECRET_KEY=                         # Get from mav
SMS_VERIFICATION=True               # Requires users to confirm SMS for their account
TEST_SMS=                           # Send SMS to TEST_PHONE during tests
DEBUG=                              # Always False for production
```


## Common Patterns
**SMS**
```python
from app.sms import SMS

# As a one off message
SMS.send('<TO_PHONE_NUMBER>', '<MESSAGE>')

# Extending the client for a particular app
class AccountSMS(SMS):
    @classmethod
    def send_book_return_reminder(cls, account):
        message = "This is my message for this text" 
        cls.send(account.phone_number, message)

account = Account.objects.get(email="jeffers@gmail.com")
AccountSMS.send_book_return_reminder(account)
```


## Troubleshooting ## 
**Migrations**

Screen Shot 2021-04-03 at 1.05.08 PM.png![image](https://user-images.githubusercontent.com/37980417/113709538-9ac5d900-96b0-11eb-97e1-0ad9a77288a5.png)

make sure your migrations are up to date. 

```
python manage.py migrate
```
