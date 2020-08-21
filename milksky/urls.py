from django.contrib import admin
from django.urls import include, path, re_path
from . import views
import skymilk

app_name = 'milksky'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('reports/', views.ReportsView.as_view(), name='reports'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('signupReport/', views.signupReport, name='signupReport'),
]