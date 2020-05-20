from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_laundrer= models.BooleanField(default=False)


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50, null=True, blank= False, unique=False, default = None)
    email = models.CharField(max_length = 50, null=True, blank= False, unique=False, default = None)
    phone_number = models.CharField(max_length = 50, null=True, blank= False, unique=False, default = None)
    dorm = models.CharField(max_length = 50, null=True, blank= False, unique=False, default = None)
    loads_done = models.IntegerField(default=0)
    def __str__(self):
        return self.customer.username


class Laundrer(models.Model):
    laundrer = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50, null=True, blank= False, unique=False, default = None)
    email = models.CharField(max_length = 50, null=True, blank= False, unique=False, default = None)
    phone_number = models.CharField(max_length = 50, null=True, blank= False, unique=False, default = None)
    dorm = models.CharField(max_length = 50, null=True, blank= False, unique=False, default = None)
    loads_completed = models.IntegerField(default=0)

    def __str__(self):
        return self.laundrer.username


class Load(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default = None )
    items_no = models.IntegerField(default =0)
    baskets_no = models.IntegerField(default =0)
    date = models.DateTimeField(default=datetime.now(), blank=True)



class Order(models.Model):
    laundrer= models.ForeignKey(Laundrer, related_name='provider', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='receiver', on_delete=models.CASCADE)
    load = models.ForeignKey(Load, on_delete=models.CASCADE)
    completed = models.BooleanField()
    rejected = models.BooleanField()
    inProgress = models.BooleanField(default = False)
