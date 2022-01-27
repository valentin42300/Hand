"""Hand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from web_front.views import UserView, LocationView, BookView, CinemaView, ProfilesListView

router = DefaultRouter()
router.register('api/users', UserView, basename='users')
router.register('api/locations', LocationView, basename='locations')
router.register('api/profiles', ProfilesListView, basename='profile')
router.register('api/book', BookView, basename='book')
router.register('api/cinema', CinemaView, basename='cinema')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='obtain_token'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('', include(router.urls)),
    # path('about-us/', views.about),
    # path('', views.index_view)
]
