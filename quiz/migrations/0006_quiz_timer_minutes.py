# Generated by Django 3.0.8 on 2023-08-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_delete_dummy'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='timer_minutes',
            field=models.IntegerField(default=100),
        ),
    ]
