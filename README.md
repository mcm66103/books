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
I reccomend using pyenv virtualenv to manage your python version and environment. This project 

[learn more about pyenv virtualenv](https://github.com/pyenv/pyenv-virtualenv)

Install python build requirements.

[instructions](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
Install the packages.

Install pyenv with homebrew
```bash
brew update
brew install pyenv
```

Add pyenv init to your shell to enable shims and autocompletion. Please make sure `eval "$(pyenv init -)"` is placed toward the end of the shell configuration file since it manipulates PATH during the initialization.
```bash
# zsh
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
```

Restart your shell so the path changes take effect. You can now begin using pyenv.
```bash
exec "$SHELL"
```

Install Python versions into `$(pyenv root)/versions`. For example, to download and install Python 2.7.8, run:
```bash
pyenv install 3.8.0
```

| Troubleshooting |
| ---------- |
| Mac os System Version: macOS 11.2.3 (20D91) has experienced build problems with this version of Python. [These instructions](https://koji-kanao.medium.com/install-python-3-8-0-via-pyenv-on-bigsur-b4246987a548) have been helpful.|

Create you python environemnt with the correct version. 
```bash
pyenv virtualenv 3.8.0 books
```

Activate your virtual environment. 
```bash
pyenv activate books
```

Install the project requirements.

```bash
pip install -r requirements.txt
```

run the migrations
```bash
python manage.py migrate
```

Export `GOOGLE_APPLICATION_CREDENTIALS` for google cloud vision API.

In a bash console...
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/PATH/TO/YOUR/PROJECT/google_credentials.json" 
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
