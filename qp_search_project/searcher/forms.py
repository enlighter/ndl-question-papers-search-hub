from django import forms
from django.contrib.auth.models import User


from .models import student

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class LoginForm(forms.Form):
    nick = forms.CharField(label='Your username', max_length=15)
    password = forms.CharField(label='password', widget=forms.PasswordInput())

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['state', 'city', 'educational_role', 'institute', 'language']
        exclude = ('user',)