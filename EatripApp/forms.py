from django import forms
from django.contrib.auth.models import User
from EatripApp.models import Restro

class UserForm(forms.ModelForm):
    '''
    email and password came from the User model,
    '''
    email = forms.CharField(max_length=100, required=True) #
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields= {"username", "password", "first_name", "last_name", "email"}

class RestroForm(forms.ModelForm):
    class Meta:
        model = Restro
        fields= {"name", "phone", "address", "logo"}