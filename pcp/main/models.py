from django.db import models


# Create your models here.
class Dolw(models.Model):
    title = models.CharField(
        "Название",
        max_length=50,
    )
    app = models.CharField(
        "Приложение",
        max_length=250,
    )

    # foto = models.ImageField("Фото")
    foto = models.CharField(
        "Фото",
        max_length=250,
    )

    ted = models.CharField(
        "Платформы",
        max_length=250,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Приложение"
        verbose_name_plural = "Приложения"
