# Generated by Django 3.0.1 on 2020-02-07 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Matchmaking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='msg',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]
