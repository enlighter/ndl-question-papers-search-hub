from django import forms
from .models import student

class UserLogin(forms.Form):
    nick = forms.CharField(label='Your username', max_length=15)
    password = forms.CharField(label='password', widget=forms.PasswordInput())

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['user', 'state', 'city', 'educational_role', 'institute', 'language']