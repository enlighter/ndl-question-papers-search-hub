from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import student


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

    class Meta(UserCreationForm.Meta):
        model = student
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'state', 'city',
                                                 'educational_role', 'institute', 'language')