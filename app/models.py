from django.db import models

# Create your models here.
from django.urls import reverse



class School(models.Model):
    name=models.CharField(max_length=100)
    Principal=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('schooldetail',kwargs={'pk':self.pk})

class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()

    def __str__(self):
        return self.sname
