from django.db import models
from django.contrib.auth.models import User # < Importing Django's built-in User model that provides us with username, email, password, first_name, and last_name fields. Based this on https://learndjango.com/tutorials/django-best-practices-referencing-user-model

class Offer(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  candidate_first_name = models.CharField(max_length=200)
  candidate_last_name = models.CharField(max_length=200)
  candidate_email_address = models.CharField(max_length=200)
  role = models.CharField(max_length=200)
  salary = models.IntegerField(default=0)

# Create your models here.
