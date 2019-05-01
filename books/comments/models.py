from django.db import models
from datetime import datetime

# Create your models here.
class comments_list(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    comment = models.CharField(max_length=500, null=True)
    date = models.DateField(default=datetime.now())