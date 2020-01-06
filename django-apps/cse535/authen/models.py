from django.db import models
from django.contrib.auth.models import User
import string

# Create your models here.
class Appuser(models.Model):
    """Model representing a User object."""
    user = models.OneToOneField(User, on_delete=models.CASCADE,default = "",null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.first_name


class Group(models.Model):
    """Model representing a User object."""
    # subject1 = models.ForeignKey(Appuser, on_delete=models.CASCADE,related_name='subject1')
    # subject2 = models.ForeignKey(Appuser,on_delete=models.CASCADE,related_name='subject2')
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    compatibility = models.FloatField(null=True, blank=True, default=None)
    score = models.FloatField(null=True, blank=True, default=None)
    #
    # def __str__(self):
    #     """String for representing the Model object."""
    #     return string(self.id)
