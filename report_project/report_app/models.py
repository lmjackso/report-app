from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserSettings(models.Model):
  # contains settings not included in 
  # the User model offered by django


class Report(models.Model):
  user = models.ForeignKey(User)
  date_created = models.DateTimeField(auto_now_add=True)



class Entry(models.Model):
  report = models.ForeignKey(Report)
  first_month = models.IntegerField(default=0)
  second_month = models.IntegerField(default=0)
  third_month = models.IntegerField(default=0)
  
