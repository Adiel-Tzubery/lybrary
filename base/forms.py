from django import forms
from django.contrib.auth.models import User


class LoginUserForm(forms.ModelForm):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['username','password']