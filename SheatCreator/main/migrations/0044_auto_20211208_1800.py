# Generated by Django 3.0.3 on 2021-12-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20211207_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='nivel',
            field=models.IntegerField(default=0, verbose_name='Nivel'),
        ),
    ]
