# Generated by Django 3.2.4 on 2021-11-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_bonificacion_raza_raza_bonificaciones_raza'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raza',
            old_name='idiomas',
            new_name='idiomas_eleccion',
        ),
        migrations.AddField(
            model_name='raza',
            name='idiomas_conocidos',
            field=models.TextField(null=True, verbose_name='Idiomas conocidos'),
        ),
    ]