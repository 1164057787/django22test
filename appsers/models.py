from django.db import models


# Create your models here.
class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=32)
    sprice = models.DecimalField(max_digits=5, decimal_places=2)
    sage = models.CharField(max_length=32)
    shome=models.CharField(max_length=32)
