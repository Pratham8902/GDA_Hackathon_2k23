import datetime
from time import time

from django.db import models




types = [('Staff','Staff'),('Visitor','Visitor')]
class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date = models.DateField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    ranking = models.CharField(max_length=20)
    profession = models.CharField(max_length=200)
    status = models.CharField(choices=types,max_length=20,null=True,blank=False,default='Visitor')
    present = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    shift = models.TimeField()
    age=models.IntegerField()

    bg=models.CharField(max_length=10)
    ephone=models.BigIntegerField()
    address=models.CharField(max_length=100)

    aadhar=models.BigIntegerField()

    languages=models.CharField(max_length=200)
    physician=models.CharField(max_length=200)
    allergies=models.CharField(max_length=200)
    height=models.DecimalField(max_digits=10,decimal_places=4)
    weight=models.DecimalField(max_digits=10,decimal_places=4)
    condition=models.CharField(max_length=200)
    drugs=models.CharField(max_length=200)



    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face

