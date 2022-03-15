from django.db import models
from django.contrib import auth
from django.utils import timezone

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

class Contact(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    subject = models.CharField(max_length=250, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + " - " + str(self.subject)