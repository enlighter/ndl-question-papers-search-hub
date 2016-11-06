from django import forms
from django.contrib.auth.models import User


from .models import student

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

class LoginForm(forms.Form):
    nick = forms.CharField(label='Your username', max_length=15)
    password = forms.CharField(label='password', widget=forms.PasswordInput())

class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # magic
        self.user = kwargs['instance'].user
        user_kwargs = kwargs.copy()
        user_kwargs['instance'] = self.user
        self.uf = UserForm(*args, **user_kwargs)
        # magic end

        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields.update(self.uf.fields)
        self.initial.update(self.uf.initial)

        # define fields order if needed
        self.fields.keyOrder = (
            'username',
            'first_name',
            'last_name',
            'email',

            'state',
            'city',
            'educational_role',
            'institute',
            'language',
        )

    def save(self, *args, **kwargs):
        # save both forms
        self.uf.save(*args, **kwargs)
        return super(RegistrationForm, self).save(*args, **kwargs)

    class Meta:
        model = student
        fields = [ 'state', 'city', 'educational_role', 'institute',
                  'language']