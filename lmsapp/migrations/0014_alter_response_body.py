# Generated by Django 4.0.5 on 2022-10-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0013_alter_response_created_alter_response_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='body',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
