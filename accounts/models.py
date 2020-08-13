from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class profile(models.Model):
    # relation with django user (already created with django)
    # or we can override the created django user
    # one to one relation and extend the django user attrs
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    city = models.ForeignKey('city',related_name='user_city',on_delete=models.CASCADE,blank=True,null=True) 
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')
    
    
    def __str__(self):
        return str(self.user)
    

# we need when create new user -> create new empty profile
# this will be done user django signals
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance )


class city(models.Model):
    name = models.CharField(max_length=30)

