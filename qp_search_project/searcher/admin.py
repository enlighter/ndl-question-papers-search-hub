from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext as _

from .models import *

class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

    class Meta(UserCreationForm.Meta):
        model = student
        fields = ('username', 'email', 'first_name', 'last_name', 'state', 'city',
                    'educational_role', 'institute', 'language', 'password1',
                    'password2')


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = student

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('username', 'email', )}),
            (_('Personal info'), {'fields': ('first_name', 'last_name',
                                    'state', 'city', 'educational_role', 'institute', 'language')}),
            (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                           'groups', 'user_permissions')}),
            (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'state', 'city',
                       'educational_role', 'institute', 'language', 'password1',
                       'password2')}
         ),
    )

admin.site.register(board)
admin.site.register(exam)

try:
    admin.site.unregister(User)
except:
    pass

admin.site.register(student, MyUserAdmin)
admin.site.register(educational_institute)
admin.site.register(search_result)
