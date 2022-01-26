# Generated by Django 4.0.1 on 2022-01-19 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
          name='Advert',
          fields=[
              ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
              ('name', models.CharField(max_length=1000)),
          ]
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
