# Generated by Django 3.0.8 on 2023-08-31 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20230831_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
