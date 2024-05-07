from django.db import models

# Customer
from django.contrib.auth.models import User

class Profile(models.Model):
    name=models.CharField(max_length=200)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    phone=models.CharField(max_length=10)
    image=models.ImageField(upload_to='images/',null=True)

    def __str__(self) -> str:
        return self.name