from django.db import models


# Create your models here.

class UserDataModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


class ShippindDataModel(models.Model):
    receiver_first_name = models.CharField(max_length=50)
    receiver_last_name = models.CharField(max_length=50)
    receiver_address = models.TextField()
