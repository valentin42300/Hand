# Generated by Django 4.0.1 on 2022-01-19 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_front', '0028_remove_cinema_user_remove_music_user_remove_tv_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
    ]