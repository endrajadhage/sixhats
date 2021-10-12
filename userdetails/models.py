from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class UserDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length = 200,blank=False, null=True, default=None)
    password = models.CharField(max_length = 200,blank=False, null=True, default=None)
    mobile_number = models.CharField(max_length=200, blank=False, null=True, default=None)

