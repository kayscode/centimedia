#from django.db import models
from django_softdelete.models import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.

class Country(models.Model):
    #id = models.BigAutoField()
    continent = models.CharField(
        max_length= 20,
        choices=[
            ("Af", "Afrique"),
            ("Eu", "Europe"),
            ("Asie", "Asie"),
            ("Amerique", "Amerique"),
            ("Oceanie", "Oceanie"),
        ],
        default="Af"
    )
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)


class Organisations(models.Model):
    #id = models.BigAutoField()
    name = models.CharField(max_length=100, null=False, unique=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    cover = models.ImageField(upload_to="uploads/organisations",null=True,blank=True)
    email = models.EmailField(unique=True)


class User(AbstractBaseUser):
    #id = models.BigAutoField()
    username = models.CharField(max_length=10, unique=True)
    avatar = models.ImageField(upload_to="uploads/avatars", null=True,blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250, blank=False, null=False)
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    account_type = models.CharField(
        max_length=20,
        choices= [
            ("admin","admin"),
            ("super admin","super admin")
        ]
    )
