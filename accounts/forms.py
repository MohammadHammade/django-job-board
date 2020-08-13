from django import forms

# to make django validation on user form
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import profile

class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

#edit profile depending on user and profile form
class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        
class profile_form(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['city','phone_number','image']
        

