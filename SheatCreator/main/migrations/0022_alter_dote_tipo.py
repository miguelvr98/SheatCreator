# Generated by Django 3.2.4 on 2021-11-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_conjuro_clase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dote',
            name='tipo',
            field=models.TextField(choices=[('General', 'General'), ('Combate', 'Combate'), ('Metamágica', 'Metamágica')], null=True, verbose_name='Tipo'),
        ),
    ]
