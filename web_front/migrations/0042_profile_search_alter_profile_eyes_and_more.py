# Generated by Django 4.0.1 on 2022-01-22 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_front', '0041_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='search',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='eyes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='origins',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
