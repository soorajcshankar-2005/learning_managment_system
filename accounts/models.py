from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES=(
        ("Trainer","Trainer"),
        ("Student","Student")

    )
    phone=models.CharField(max_length=30,unique=True)
    role=models.CharField(max_length=50,choices=ROLE_CHOICES)
    



class TrainerProfile(models.Model):
    subject=models.CharField(max_length=100,null=True)
    experience=models.CharField(max_length=100,null=True)
    email=models.EmailField(unique=True,null=True)
    owner=models.OneToOneField(User, on_delete=models.CASCADE,related_name="tr_profile")


class StudentProfile(models.Model):
    GENDER_CHOICES=(
        ("male","male"),
        ("female","female"),
        ("others","others")
    )
    age=models.PositiveBigIntegerField(null=True)

    gender=models.CharField(max_length=50,choices=GENDER_CHOICES,default="male")

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="st_profile")

