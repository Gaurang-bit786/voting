# Generated by Django 4.0.4 on 2022-05-18 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_delete_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('roll_no', models.CharField(max_length=150)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branche')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]
