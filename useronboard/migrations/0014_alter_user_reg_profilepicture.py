# Generated by Django 4.0.5 on 2022-09-26 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useronboard', '0013_remove_userlogin_email_userlogin_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reg',
            name='profilepicture',
            field=models.ImageField(default='images/userprofilepic.png', null=True, upload_to='profilemages'),
        ),
    ]
