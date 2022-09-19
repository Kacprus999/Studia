from django.db import models

# Create your models here.

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    male = 'Male'
    female = 'Female'
    other = 'Other'
    sex_choices =[
        (male, 'Male'),
        (female, 'Female'),
        (other, 'Other'),]
    sex = models.CharField(choices = sex_choices,max_length=6,)
    role_id = models.ForeignKey('Role',on_delete=models.CASCADE)
    isDeleted = models.BooleanField(default=False)
    def __str__(self):
        return self.login + ' ' + self.fname + ' ' + self.lname 
    
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa_roli = models.CharField(max_length=200) 
    def __str__(self):
        return self.nazwa_roli