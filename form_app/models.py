from django.db import models
# Create your models here.
class Student(models.Model):
    f_name=models.CharField(max_length=256)
    l_name=models.CharField(max_length=256)
    email=models.EmailField()
