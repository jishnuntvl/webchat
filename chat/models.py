from datetime import datetime
from django.utils import timezone
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
    
class Message(models.Model):
    value=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now,blank=True)
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    time = models.TimeField(default=timezone.now,blank=True)
    def __str__(self):
        return self.value