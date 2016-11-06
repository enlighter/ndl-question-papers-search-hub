from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import student

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = student
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'state', 'city',
                                                 'educational_role', 'institute', 'language')