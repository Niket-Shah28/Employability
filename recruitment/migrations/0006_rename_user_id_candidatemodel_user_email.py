# Generated by Django 4.0.3 on 2023-03-11 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0005_rename_user_email_candidatemodel_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidatemodel',
            old_name='User_Id',
            new_name='User_email',
        ),
    ]
