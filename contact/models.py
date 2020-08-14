from django.db import models

# Create your models here.

class info(models.Model):
    place = models.CharField(max_length=50,blank=True,null=True)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=254,blank=True,null=True)

    # def __str__(self):
    #     return self.name