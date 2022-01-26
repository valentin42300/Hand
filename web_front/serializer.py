from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import Location, Profile, Book, Cinema, Music, Tv


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
        ]


class ProfileListSerializer(serializers.ModelSerializer):
    user = UserListSerializer

    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'location',
            'origins',
            'eyes',
            'search',
            'alcohol',
            'birth_date',
            'tobacco',
            'children',
            'silhouette',
            'hairs',
            'sexuality',
            'relation',
            'status',
            'disability',
            'gender',
            'size',
            'advert_search',
            'advert',
            'tv',
            'music',
            'cinema',
            'book',
        ]

    def get_user(self, instance):
        queryset = instance.user
        serializer = UserListSerializer(queryset)
        return serializer.data

    def validate_user(self, value):
        if value.is_superuser:
            raise serializers.ValidationError('Pas de admin')
        return value


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'country',
            'country_code',
            'city',
            'zip_code',
            'register_ip',
            'connected_ip',
            'lat',
            'lon',
            'asLocation',
            'region',
            'isp',
            'timezone',
            'org',
        ]


class BookListSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer

    class Meta:
        model = Book
        fields = [
            'profile',
            'name'
        ]


class CinemaListSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer

    class Meta:
        model = Cinema
        fields = [
            'profile',
            'name'
        ]


class MusicListSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer

    class Meta:
        model = Music
        fields = [
            'profile',
            'name'
        ]


class TvListSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer

    class Meta:
        model = Tv
        fields = [
            'profile',
            'name'
        ]


class ProfileDetailSerializer(ModelSerializer):

    user = UserListSerializer()
    location = LocationSerializer()

    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'location',
            'origins',
            'eyes',
            'search',
            'alcohol',
            'birth_date',
            'tobacco',
            'children',
            'silhouette',
            'hairs',
            'sexuality',
            'relation',
            'status',
            'disability',
            'gender',
            'size',
            'advert_search',
            'advert',
            'tv',
            'music',
            'cinema',
            'book',
        ]
