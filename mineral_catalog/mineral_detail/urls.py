from django.urls import path

from . import views

urlpatterns = [
    path('', views.mineral_detail, name='mineral_detail'),
]