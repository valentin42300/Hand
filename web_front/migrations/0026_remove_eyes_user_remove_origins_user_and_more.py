# Generated by Django 4.0.1 on 2022-01-19 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_front', '0025_remove_advertsearch_user_remove_disability_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eyes',
            name='user',
        ),
        migrations.RemoveField(
            model_name='origins',
            name='user',
        ),
        migrations.RemoveField(
            model_name='search',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tobacco',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userbirthdate',
            name='user',
        ),
        migrations.DeleteModel(
            name='Alcohol',
        ),
        migrations.DeleteModel(
            name='Eyes',
        ),
        migrations.DeleteModel(
            name='Origins',
        ),
        migrations.DeleteModel(
            name='Search',
        ),
        migrations.DeleteModel(
            name='Tobacco',
        ),
        migrations.DeleteModel(
            name='UserBirthDate',
        ),
    ]
