from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fields/', views.fields_index, name='fields_index'),
    path('fields/<int:field_id>/', views.fields_detail, name='fields_detail'),
    path('fields/create/', views.FieldCreate.as_view(), name='fields_create'),
    path('fields/<int:pk>/delete/', views.FieldDelete.as_view(), name='fields_delete'),
    path('dinos/<int:dino_id>/', views.dinos_detail, name='dinos_detail'),
    path('hatch_dino/', views.hatch_dino, name='hatch_dino'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]