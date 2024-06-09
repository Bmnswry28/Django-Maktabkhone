from django.db import models
# Create your models here.
class UserForm(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=100)
class ResetPasswordForm(models.Model):
    email = models.EmailField()