# Generated by Django 4.0.5 on 2022-09-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useronboard', '0002_alter_stageonesignup_track'),
    ]

    operations = [
        migrations.CreateModel(
            name='stagetwosignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_full', models.CharField(max_length=255)),
                ('github', models.URLField(blank=True, max_length=255, null=True)),
                ('linkedIn', models.URLField(max_length=255)),
                ('twitter', models.URLField(max_length=255)),
                ('facebook', models.URLField(blank=True, max_length=255, null=True)),
                ('instagram', models.URLField(blank=True, max_length=255, null=True)),
                ('portfoliowebsite', models.URLField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
