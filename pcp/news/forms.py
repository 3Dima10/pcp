from .models import Aweitr
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class Ahop(ModelForm):
    class Meta:
        model = Aweitr
        fields = ["title", "anons", "text", "data"]

        widgets = {
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "Название статьй"},
            ),
            "anons": TextInput(
                attrs={"class": "form-control", "placeholder": "Анонс статьй"},
            ),
            "text": Textarea(
                attrs={"class": "form-control", "placeholder": "Текст статьй"},
            ),
            "data": DateTimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Дата публикацый",
                },
            ),
        }
