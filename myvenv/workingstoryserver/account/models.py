from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


# Create your dto here.


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employee')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.user.first_name, self.user.last_name)
        return full_name.strip()

    def get_email(self):
        email = '%s' % self.user.email
        return email.strip()
