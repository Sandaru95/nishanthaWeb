from django.db import models
from django.contrib.auth.models import User

class UserSignal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)

class UserGoogle(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    logged_in = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} : {self.username}"

class UserFacebook(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    logged_in = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} : {self.username}"

class UserTwitter(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    logged_in = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} : {self.username}"
