# Generated by Django 3.0.8 on 2023-08-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_remove_program_paystatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='fees',
            field=models.IntegerField(null=True),
        ),
    ]
