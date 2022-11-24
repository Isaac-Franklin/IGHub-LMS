# Generated by Django 4.0.5 on 2022-09-23 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useronboard', '0009_user_reg_delete_stageonesignup_delete_stagetwosignup'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_reg',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_reg',
            name='profilepicture',
            field=models.ImageField(null=True, upload_to='profilemages', verbose_name=''),
        ),
    ]
