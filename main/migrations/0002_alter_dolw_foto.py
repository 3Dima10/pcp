# Generated by Django 5.0.1 on 2024-01-31 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolw',
            name='foto',
            field=models.CharField(max_length=250, verbose_name='Фото'),
        ),
    ]
