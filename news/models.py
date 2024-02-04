from django.db import models


# Create your models here.
class Aweitr(models.Model):
    title = models.CharField(
        "Название",
        max_length=50,
    )
    anons = models.CharField(
        "Анонс",
        max_length=250,
    )

    text = models.TextField("Текст")
    data = models.DateTimeField("Дата")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
