"""IQBACK2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from rest_framework.authtoken import views

#usuarios 
from usuarios.usuarios import UserApi
from usuarios.views import LogoutView, LoginView, cambiarClave




urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',include(('basedata.urls'))),
    path('clientes/',include(('clientes.urls'))),
    path('api_generate_token/', views.obtain_auth_token),
    path('password_change/', cambiarClave.as_view(), name='password_change'),

    path('api/1.0/create_user', UserApi.as_view(), name = "api_create_user"),
    path('logout/', LogoutView.as_view(), name= 'Logout'),
    path('logout2/', LoginView.as_view(), name= 'Logout'),
]
