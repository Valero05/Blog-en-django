# Generated by Django 4.2 on 2023-07-18 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_perfil_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='descripcion',
            field=models.TextField(default='Lorem ipsum', max_length=1500),
        ),
    ]