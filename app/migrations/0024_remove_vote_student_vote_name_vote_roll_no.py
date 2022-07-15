# Generated by Django 4.0.4 on 2022-05-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_vote_name_remove_vote_roll_no_student_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='student',
        ),
        migrations.AddField(
            model_name='vote',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='roll_no',
            field=models.CharField(max_length=150, null=True),
        ),
    ]