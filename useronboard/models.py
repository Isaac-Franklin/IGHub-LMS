from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# //////
# from . import models


# Create your models here.


active_user_models = get_user_model()


class user_reg(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    # track = MultiSelectField(choices=TRACK_CHOICES)
    track = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True, blank=True)
    dateofbirth = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200)
    repassword = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
# STAGE TWO
    github = models.URLField(max_length=255, blank=True, null=True)
    linkedIn = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    portfoliowebsite = models.URLField(max_length=255, blank=True, null=True)

# STAGE THREE
    profilepicture = models.ImageField(
        upload_to='profileimages', null=True, default="images/userprofilepic.png")
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Userlogin(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
