# Generated by Django 4.0.5 on 2022-09-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0007_rename_selec_track_video_upload_select_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_upload',
            name='Video_Description',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='video_upload',
            name='Video_Title',
            field=models.CharField(max_length=10),
        ),
    ]
