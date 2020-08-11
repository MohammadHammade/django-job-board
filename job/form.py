from django import forms
from .models import apply

#if the form is not for model
# class apply_form(forms.form)


#if the form is for model
class apply_form(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['name','email','website','cv','cover_letter']
        
