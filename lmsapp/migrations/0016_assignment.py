# Generated by Django 4.0.5 on 2022-10-02 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lmsapp', '0015_quizes_prize_alter_response_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('track', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=300)),
                ('detailed_description', models.CharField(max_length=30000)),
                ('resources', models.CharField(max_length=1000)),
                ('mode_of_submission', models.CharField(max_length=200)),
                ('task_point', models.IntegerField(max_length=200)),
                ('data_of_submission', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
