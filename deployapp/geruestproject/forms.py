from django import forms
from django.contrib.auth.models import User  # use ModelForm if closely working with database!

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model= User
        fields= ('first_name', 'last_name', 'email', 'username', 'password',)    #from User._meta.get_fields()
