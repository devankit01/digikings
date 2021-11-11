from django.db import models

from django.contrib.auth.models import User


# User Have - Firstname,Lastname,username,email,password and Profile is connected to user
# User Profile

class Profile(models.Model):
    Genders=(
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others")
    )
    auth_token = models.CharField(max_length=100,null = True)
    is_verified = models.BooleanField(default=False)
    gender = models.CharField(max_length=20,choices=Genders,null = True,default=None)
    phone = models.CharField(max_length=30)
    pin_code=models.IntegerField(null=True)
    country=models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100 ,null = True)
    username = models.ForeignKey(User , on_delete = models.CASCADE)

    def __str__(self):
        return str(self.username.first_name) + " " + str(self.username.last_name)
