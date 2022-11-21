from django.db import models
from django.utils.timezone import now


class MyBoard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=1000)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField(default=now)