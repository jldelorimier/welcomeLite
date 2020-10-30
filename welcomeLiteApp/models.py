from django.db import models
from django.contrib.auth.models import User # < Importing Django's built-in User model that provides us with username, email, password, first_name, and last_name fields. Based this on https://learndjango.com/tutorials/django-best-practices-referencing-user-model

# class User(models.Model):
#   username = models.CharField(max_length=200)

class Offer(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  candidate_first_name = models.CharField(max_length=200)
  candidate_last_name = models.CharField(max_length=200)
  candidate_email_address = models.CharField(max_length=200)
  role = models.CharField(max_length=200)
  salary = models.IntegerField(default=0)
  # salary_string = str(salary)
  def __str__(self):
    return self.candidate_first_name + ", " + self.candidate_last_name + ", " + self.candidate_email_address + ", " + self.role
    #  + ", " + self.salary_string  <<< This was giving me back <django.db.models.fields.IntegerField> in the interactive console

# Create your models here.
