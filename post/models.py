from django.db import models

# Create your models here.

class table1(models.Model):
    userid = models.CharField(max_length=20)
    uploaded_time = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    price = models.FloatField()
    year = models.FloatField()
    county_name = models.CharField(max_length=20)
    state_code = models.CharField(max_length=10)
    state_name = models.CharField(max_length=20)