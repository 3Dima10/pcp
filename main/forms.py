from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from .models import *

# from .models import Aweitr
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


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


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={"class": "form-input", "id": "form-input1", "placeholder": "Логин"}
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "id": "form-input2", "placeholder": "Пароль"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password1")


class Ahop(ModelForm):
    class Meta:
        model = Dolw
        fields = ["title", "app", "foto", "ted"]

        widgets = {
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "Название Приложения"},
            ),
            "app": TextInput(
                attrs={"class": "form-control", "placeholder": "Сылка на приложение"},
            ),
            "foto": TextInput(
                attrs={"class": "form-control", "placeholder": "Фото приложения"},
            ),
            "ted": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Платформа",
                },
            ),
        }
