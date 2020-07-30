from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="images/")

