# Generated by Django 4.0.1 on 2022-01-24 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_front', '0053_alter_profile_advert_alter_profile_advert_search_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='user',
        ),
        migrations.AddField(
            model_name='location',
            name='profile',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='location', serialize=False, to='web_front.profile'),
            preserve_default=False,
        ),
    ]
