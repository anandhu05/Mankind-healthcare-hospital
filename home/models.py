
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

class departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_description = models.TextField()
    def __str__(self):
        return self.dept_name

class doctors(models.Model):
    doct_name=models.CharField(max_length=100)
    doct_specialization=models.CharField(max_length=250)
    doct_dept= models.ForeignKey(departments,on_delete=models.CASCADE)
    doct_image=models.ImageField(upload_to='doctors')
