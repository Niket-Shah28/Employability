# Generated by Django 4.0.3 on 2023-03-11 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_model',
            old_name='Email',
            new_name='email',
        ),
    ]
