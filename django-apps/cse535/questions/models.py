
from django.db import models
from authen.models import Appuser,Group
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default =1)
    solution1 = models.CharField(max_length=50)
    solution2 = models.CharField(max_length=100)
    solution3 = models.CharField(max_length=100)
    solution4 = models.CharField(max_length=100)
    solution5 = models.CharField(max_length=100)
    solution6 = models.CharField(max_length=100)
    solution7 = models.CharField(max_length=100)
    solution8 = models.CharField(max_length=100)
    solution9 = models.CharField(max_length=100)
    solution10 = models.CharField(max_length=100)
    solution11 = models.CharField(max_length=100)
    solution12 = models.CharField(max_length=100)
    solution13 = models.CharField(max_length=100)
    solution14 = models.CharField(max_length=100)
    solution15 = models.CharField(max_length=100)
    solution16 = models.CharField(max_length=100)
    solution17 = models.CharField(max_length=100)
    solution18 = models.CharField(max_length=100)
    solution19 = models.CharField(max_length=100)
    solution20 = models.CharField(max_length=100)
