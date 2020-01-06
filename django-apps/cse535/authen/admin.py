from django.contrib import admin

# Register your models here.
from .models import Appuser
from authen.models import Group

admin.site.register(Appuser)
admin.site.register(Group)
