from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={"class": "form-input", 
                   "id": "form-input3", 
                   "placeholder": "Логин"}
        ),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", 
                   "id": "form-input2", 
                   "placeholder": "Пароль"}
        ),
    )
    password2 = forms.CharField(
        label="Павтор пароля",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "id": "form-input1",
                "placeholder": "Павтор пароля",
            }
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
