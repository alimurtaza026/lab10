"""lab10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import UserDataFormView, HomeView, UserDataListView, ShippingDataFormView, ShippingDataListView
app_name = 'core'
urlpatterns = [
    path('userdataform/', UserDataFormView.as_view(), name='userdataform'),
    path('', HomeView.as_view(), name='homepage'),
    path('userdetails/', UserDataListView.as_view(), name='userdatalist'),
    path('shippingdataform/', ShippingDataFormView.as_view(), name='shippingform'),
    path('shippingdetails/', ShippingDataListView.as_view(), name='shippingdatalist')

]
