# Generated by Django 4.0.1 on 2022-01-19 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('web_front', '0016_tobacco_userbirthdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alcohol',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_alcohol', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]