from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = Apps
        fields ='all'

class LoginForm(forms.ModelForm):
    class Meta:
        model = Apps
        fields =['first_name', 'password']    

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '_all_'