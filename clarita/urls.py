"""clarita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include 
from django.conf.urls  import url,include

from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from hostal import views, forms, models




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('comedor', views.comedor, name='comedor'),
    path('comedorMenu', views.comedorMenu, name='comedorMenu'),
    path('comedorPlatos',views.comedorPlatos, name='comedorPlatos'),
    path('comedorOK', views.Comedor_OK, name='comedorOK'),
    path('comedorOK2', views.Comedor_OK2, name='comedorOK2'),
    path('clienteOK', views.cliente_OK, name='clienteOK'),
    path('registro',views.cliente, name='registro'),
    


    



]
