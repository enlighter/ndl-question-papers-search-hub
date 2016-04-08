from django import forms

class UserLogin(forms.Form):
    nick = forms.CharField(label='Your username', max_length=15)
    password = forms.CharField(label='password', widget=forms.PasswordInput())
