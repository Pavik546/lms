# Generated by Django 3.0.8 on 2023-08-23 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_program_paystatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='paystatus',
        ),
    ]
