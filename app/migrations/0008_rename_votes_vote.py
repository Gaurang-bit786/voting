# Generated by Django 4.0.4 on 2022-05-17 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_votes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
    ]
