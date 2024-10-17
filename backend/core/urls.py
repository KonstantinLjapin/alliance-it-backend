from django.contrib import admin
from django.urls import path
from rest_framework import permissions

"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from geosuport.views import GEOView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    #path('api/users/register', RegisterView.as_view(), name='register'),
    #path('api/users/login', LoginView.as_view(), name='login'),
    #path('api/users/logout', LogoutView.as_view(), name='logout'),
    #path('api/users/profile', UserProfileView.as_view(), name='profile'),
    #path('api/bikes/list', ListBikeView.as_view(), name='bikes'),
    #path('api/bikes/rent_start', RentStartView.as_view(), name='rent_start'),
    #path('api/bikes/rent_end', RentEndView.as_view(), name='rent_end'),

]
