# Generated by Django 4.0.1 on 2022-01-20 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('web_front', '0035_delete_location_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_location', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('country', models.CharField(max_length=50)),
                ('country_code', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('register_ip', models.CharField(max_length=100)),
                ('connected_ip', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=50)),
                ('lon', models.CharField(max_length=50)),
                ('asLocation', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=150)),
                ('isp', models.CharField(max_length=100)),
                ('timezone', models.CharField(max_length=50)),
                ('org', models.CharField(max_length=100)),
            ],
        ),
    ]
