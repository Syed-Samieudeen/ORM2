from django.db import models

from django.contrib import admin
class car(models.Model):
    car_name=models.CharField(max_length=100)
    car_model=models.CharField(max_length=100)
    car_price=models.IntegerField()
    release = models.DateField()
# Create your models here.

class caradmin(admin.ModelAdmin):
    list_display = ('car_name','car_model','car_price','release')