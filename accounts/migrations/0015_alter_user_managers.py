# Generated by Django 3.2.20 on 2023-08-17 06:24

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
