# Generated by Django 3.0.3 on 2022-02-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220203_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dote',
            name='ataque_base',
            field=models.IntegerField(default=0, null=True, verbose_name='Ataque base'),
        ),
        migrations.AlterField(
            model_name='dote',
            name='nivel',
            field=models.IntegerField(default=0, null=True, verbose_name='Nivel'),
        ),
    ]
