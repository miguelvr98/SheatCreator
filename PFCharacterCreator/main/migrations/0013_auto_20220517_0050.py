# Generated by Django 3.0.3 on 2022-05-16 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_clase_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='descripcion',
            field=models.TextField(null=True, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='raza',
            name='descripcion',
            field=models.TextField(null=True, verbose_name='Descripción'),
        ),
    ]