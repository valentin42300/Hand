from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    if age < 18:
        raise ValidationError('Erreur date')
    return birth_date


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=False, related_name='user')
    origins = models.fields.CharField(max_length=100, name='origins', null=True, blank=True)
    eyes = models.fields.CharField(max_length=100, name='eyes', null=True, blank=True)
    search = models.fields.CharField(max_length=100, name='search', null=True, blank=True)
    alcohol = models.fields.CharField(max_length=100, null=True, blank=True, name='alcohol')
    birth_date = models.fields.DateField(null=True, blank=True, name='birth_date', validators=[calculate_age])
    tobacco = models.fields.CharField(max_length=100, null=True, blank=True, name='tobacco')
    children = models.fields.CharField(max_length=100, null=True, blank=True, name='children')
    silhouette = models.fields.CharField(max_length=100, null=True, blank=True, name='silhouette')
    hairs = models.fields.CharField(max_length=100, null=True, blank=True, name='hairs')
    sexuality = models.fields.CharField(max_length=100, null=True, blank=True, name='sexuality')
    relation = models.fields.CharField(max_length=100, null=True, blank=True, name='relation')
    status = models.fields.CharField(max_length=100, null=True, blank=True, name='status')
    disability = models.fields.CharField(max_length=100, null=True, blank=True, name='disability')
    gender = models.fields.CharField(max_length=100, null=True, blank=True, name='gender')
    size = models.fields.IntegerField(null=True, blank=True, name='size', validators=[MinValueValidator(120)])
    advert_search = models.fields.TextField(null=True, blank=True, name='advert_search')
    advert = models.fields.TextField(null=True, blank=True, name='advert')

    def __str__(self):
        return f'{self.user.username}'


class Tv(models.Model):
    name = models.fields.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tv', null=False, blank=False)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.fields.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False, related_name='music')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    name = models.fields.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False, related_name='cinema')

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.fields.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False, related_name='book')

    def __str__(self):
        return self.name


class Location(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True, related_name='location')
    country = models.fields.CharField(max_length=50, name='country')
    country_code = models.fields.CharField(max_length=5, name='country_code')
    city = models.fields.CharField(max_length=50, name='city')
    zip_code = models.fields.CharField(max_length=10, name='zip_code')
    register_ip = models.fields.CharField(max_length=100, name='register_ip')
    connected_ip = models.fields.CharField(max_length=100, name='connected_ip')
    lat = models.fields.CharField(max_length=50, name='lat')
    lon = models.fields.CharField(max_length=50, name='lon')
    asLocation = models.fields.CharField(max_length=100, name='asLocation', null=True, blank=True)
    region = models.fields.CharField(max_length=150, name='region')
    isp = models.fields.CharField(max_length=100, name='isp', null=True, blank=True)
    timezone = models.fields.CharField(max_length=50, name='timezone', null=False, blank=True)
    org = models.fields.CharField(max_length=100, name='org', null=True, blank=True)

    def __str__(self):
        return f'{self.city} / {self.country}'
