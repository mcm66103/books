from django.conf import settings

class EnvHelper():
    def __init__(self):
        self.env = settings.ENV

    def is_env(self, env):
        return self.env == env

    def is_development(self):
        return self.env == 'development'

    def is_production(self):
        return self.env == 'production'