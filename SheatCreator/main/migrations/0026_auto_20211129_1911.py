# Generated by Django 3.2.4 on 2021-11-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_dote_prerrequisito_raza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dote',
            name='prerrequisito_raza',
        ),
        migrations.AddField(
            model_name='dote',
            name='prerrequisito_raza',
            field=models.ManyToManyField(to='main.Raza'),
        ),
    ]
