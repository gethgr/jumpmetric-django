from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



# Create your models here.

class TypeOfTrialChoices(models.TextChoices):
    Choose = '-'
    cmj = 'CMJ'
    sj = 'SJ'
    iso = 'ISO'
    dj = 'DJ'


class Trial(models.Model):
    fullname = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.FloatField()
    age = models.IntegerField()
    email = models.CharField(max_length=100, blank=True, null=True)
    occupy = models.CharField(max_length=100,blank=True, null=True)
    type_of_trial = models.CharField(max_length=10, choices=TypeOfTrialChoices.choices, default=TypeOfTrialChoices.Choose)
    drop_jump_height = models.FloatField(blank=True, null=True)
    filename = models.CharField(blank=True, null=True,max_length=200)
    trial_csv = models.FileField(upload_to ="trials_csv") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return str(self.fullname)


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    occupy = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username
    