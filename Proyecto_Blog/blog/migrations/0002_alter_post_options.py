# Generated by Django 4.2 on 2023-07-18 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-titulo']},
        ),
    ]
