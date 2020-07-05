from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    balance = models.FloatField(default=0)

class Transaction(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_sent")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_received")
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Usage(models.Model):
    api_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

