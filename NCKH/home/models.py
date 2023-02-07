import datetime

from django.db import models

# Create your models here.
class light_control(models.Model):
    value = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.value)

class fan_control(models.Model):
    value_fan = models.TextField()
    time_fan = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.value_fan)

class tv_control(models.Model):
    value_tv = models.TextField()
    time_tv = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.value_tv)

class dh_control(models.Model):
    value_dh = models.TextField()
    time_dh = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.value_dh)