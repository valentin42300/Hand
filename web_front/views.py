from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from web_front.serializer import UserListSerializer, LocationSerializer, \
    ProfileListSerializer, BookListSerializer, CinemaListSerializer, ProfileDetailSerializer
from web_front.models import Location, Profile, Book, Cinema


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class UserView(ReadOnlyModelViewSet):
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(is_superuser=False)


class LocationView(ModelViewSet):
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Location.objects.all()


class ProfileView(ModelViewSet):
    serializer_class = ProfileListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.all()


class BookView(ModelViewSet):
    serializer_class = BookListSerializer

    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.all()


class CinemaView(ModelViewSet):
    serializer_class = CinemaListSerializer

    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cinema.objects.all()


class ProfilesListView(ModelViewSet):
    serializer_class = ProfileDetailSerializer

    def get_queryset(self):
        return Profile.objects.all()


def index_view(request):
    return render(request, 'web_front/index.html')
