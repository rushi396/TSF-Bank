from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    id=models.IntegerField(default=0,primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    accbal = models.IntegerField()

class Transfer(models.Model):
    sender = models.CharField(max_length=200, null=True)
    reciever = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(default=0)
    date_tran = models.DateTimeField(auto_now_add=True)