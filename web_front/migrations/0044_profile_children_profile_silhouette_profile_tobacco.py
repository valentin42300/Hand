# Generated by Django 4.0.1 on 2022-01-22 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_front', '0043_profile_alcohol_profile_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='children',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='silhouette',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='tobacco',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
