from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
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


def create_trainer_profile(sender,instance,created,**kwargs):

    if created and instance.role=="Trainer":

        TrainerProfile.objects.create(owner = instance)

post_save.connect(create_trainer_profile,sender = User)

def create_student_profile(sender,instance,created,**kwargs):

    if created and instance.role=="Student":

        StudentProfile.objects.create(owner = instance)

post_save.connect(create_student_profile,sender = User)


