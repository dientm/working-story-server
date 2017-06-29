from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your dto here.

class WorkLog(models.Model):
    ACTION_CHOICES = (
        (u'1', u'start working'),
        (u'2', u'finish working'),
        (u'3', u'annual leave'),
        (u'4', u'public holiday'),
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    action_on = models.DateTimeField(auto_now_add =True)
    location = models.CharField(max_length=255, blank=True)
    report = models.TextField(blank=True)

    # def __init__(self, user, action, location, report):
    #     self.user = user
    #     self.action = action
    #     self.action_on = action_on
    #     self.location = location
    #     self.report = report

class LocalBeacon(models.Model):
    uuid = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    major = models.CharField(max_length=5, blank=True)
    minor = models.CharField(max_length=5, blank=True)
    location = models.CharField(max_length=255, blank=False)

    def as_json(self):
        return dict(
            uuid=self.uuid,
            location=self.location,
            name=self.name,
            major=self.major,
            minor=self.minor)
