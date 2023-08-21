from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fields/', views.fields_index, name='fields_index'),
    path('fields/<int:field_id>/', views.fields_detail, name='fields_detail'),
    path('fields/create/', views.FieldCreate.as_view(), name='fields_create'),
    path('fields/<int:pk>/delete/', views.FieldDelete.as_view(), name='fields_delete'),
    path('fields/<int:field_id>/add_dino/', views.add_dino, name='add_dino'),
    path('dinos/<int:dino_id>/', views.dinos_detail, name='dinos_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]