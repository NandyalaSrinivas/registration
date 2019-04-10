# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=200, null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    email_id = models.EmailField(max_length=200)

class Student(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField( null=True,blank=True)
    mobile_no = models.BigIntegerField(max_length=12)
    address = models.TextField (max_length=500)
    roll_no = models.IntegerField(max_length=10)
    d_join_date = models.DateTimeField( null=True,blank=True)

class Documents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ssc = models.FileField(upload_to='media/upload/%y/%m/%d/', null=True,blank=True)
    inter = models.FileField(upload_to='media/upload/%y/%m/%d/', null=True,blank=True)
    degree = models.FileField(upload_to='media/upload/%y/%m/%d/', null=True, blank=True)
    mca = models.FileField(upload_to='media/upload/%y/%m/%d/', null=True, blank=True)