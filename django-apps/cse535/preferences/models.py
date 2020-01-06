from django.db import models
from authen.models import Appuser

# Create your models here.
class preferences(models.Model):
    userid = models.OneToOneField(Appuser, on_delete=models.CASCADE, default =1)
    topic1 = models.CharField(max_length=50)
    topic2 = models.CharField(max_length=100)
    topic3 = models.CharField(max_length=100)
    topic4 = models.CharField(max_length=100)
    # topic5 = models.CharField(max_length=100)
