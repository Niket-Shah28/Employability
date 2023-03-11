# Generated by Django 4.0.3 on 2023-03-11 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_rename_email_user_model_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='Category',
            field=models.CharField(choices=[('Candidate', 'CANDIDATE'), ('Recruiter', 'RECRUITER')], max_length=50),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='Gender',
            field=models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Other', 'OTHER')], max_length=30),
        ),
        migrations.CreateModel(
            name='CandidateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_of_birth', models.DateField()),
                ('Gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Other', 'OTHER')], max_length=30)),
                ('Qualification', models.CharField(choices=[('Graduation', 'GRADUATION'), ('Senior Secendory (XII)', 'SENIOR SECENDORY (XII)'), ('Secendory (X)', 'SECENDORY (X)'), ('Diploma', 'DIPLOMA'), ('Post Graduation', 'POST GRADUATION'), ('PHD', 'PHD')], max_length=100)),
                ('Skills', models.CharField(max_length=100)),
                ('Resume', models.FileField(upload_to='statsicfiles/')),
                ('Years_of_Experience', models.IntegerField()),
                ('Expected_Salary', models.IntegerField()),
                ('User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
