from django.db import models

class Event(models.Model):
    fname = models.CharField(max_length=10,verbose_name='first name')
    lname = models.CharField(max_length=10,verbose_name='last name')
    mobile_number = models.IntegerField()
    venue = models.CharField(max_length=10)
    date = models.DateField()
    address = models.CharField(max_length=10)

