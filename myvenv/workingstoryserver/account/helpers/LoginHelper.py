from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

user_credentials = ['request', 'username', 'password']


class LoginHelper:
    def __init__(self, **kwargs):
        for key in user_credentials:
            self.key = kwargs[key]

    def do_login(self):
        user = authenticate(self.request, username=self.username, password=self.password)
        if user is not None:
            login(self.request, user)