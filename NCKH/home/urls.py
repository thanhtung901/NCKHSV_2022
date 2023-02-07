from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.myViews.as_view(), name='myViews'),
    path('lights/', views.Lights_config.as_view(), name='load'),
    path('fan/', views.fan_config.as_view(), name='fan'),
    path('tv/', views.tv_config.as_view(), name='tv'),
    path('dh/', views.dh_config.as_view(), name='dh'),
]
