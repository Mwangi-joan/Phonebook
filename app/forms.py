from django import forms
from .models import Phonebook
from django.contrib.auth.models import User

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Phonebook
        fields = ['name','emailaddress','phonenumber','gender','photo']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']