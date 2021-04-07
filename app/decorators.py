from django.conf import settings

def require_test_sms(func):
    def func_wrapper(*args, **kwargs):
        if settings.TEST_SMS == True:
            return func(*args, **kwargs)

        else: 
            print("\n\nskipping SMS test because TEST_SMS is turned off.\n\n")
            pass

    return func_wrapper