# Generated by Django 4.0.4 on 2022-05-19 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_student_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='active',
            field=models.BooleanField(),
        ),
    ]