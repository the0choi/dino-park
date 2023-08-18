from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fields/', views.fields_index, name='fields_index'),
    path('fields/<int:field_id>/', views.fields_detail, name='fields_detail'),
    path('dinos/<int:dino_id>/', views.dinos_detail, name='dinos_detail'),
]
