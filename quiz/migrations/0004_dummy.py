# Generated by Django 3.0.8 on 2023-08-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20230823_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='dummy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=100)),
                ('courset', models.CharField(max_length=100)),
                ('coursep', models.CharField(max_length=100)),
                ('quizc', models.CharField(max_length=100)),
                ('quizt', models.CharField(max_length=100)),
                ('total', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('maxscore', models.IntegerField(default=0)),
            ],
        ),
    ]
