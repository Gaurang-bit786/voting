# Generated by Django 4.0.4 on 2022-05-17 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_votes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Votes',
        ),
    ]
