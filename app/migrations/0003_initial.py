# Generated by Django 4.0.4 on 2022-05-17 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_mca'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('roll_no', models.CharField(max_length=150)),
            ],
        ),
    ]
