import json
import datetime

class Account:
    def __init__(self, **kwargs):
        params = ["username", "email", "last_login", "name"]
        for key in params:
            self.key = kwargs[key]

    def __init__(self, user):
        self.username = user.username
        self.name = user.first_name + user.last_name
        self.email = user.email
        self.last_login = str(user.last_login)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


