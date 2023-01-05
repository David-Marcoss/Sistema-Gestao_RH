from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserChangeForm(UserCreationForm):
    email = forms.fields.EmailField()

    #definição de valores padrao
    class Meta:
        model = User  # model padrao de usuarios do django
        fields = fields = ['username','email','password1','password2']
