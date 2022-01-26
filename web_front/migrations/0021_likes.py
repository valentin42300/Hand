# Generated by Django 4.0.1 on 2022-01-19 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_front', '0020_alter_visits_user_from_alter_visits_user_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user_like_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like_from', to=settings.AUTH_USER_MODEL)),
                ('user_like_to', models.ForeignKey(on_delete=django.db.models.fields.CharField, related_name='user_like_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
