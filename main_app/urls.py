from django.urls import path, include
from . import views

# URL patterns for different views and endpoints
urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # About page
    path('about/', views.about, name='about'),
    
    # Fields index page (list of fields)
    path('fields/', views.fields_index, name='fields_index'),
    
    # Field detail page with a specific field's details
    path('fields/<int:field_id>/', views.fields_detail, name='fields_detail'),
    
    # Create a new field
    path('fields/create/', views.FieldCreate.as_view(), name='fields_create'),
    
    # Delete a field using its primary key
    path('fields/<int:pk>/delete/', views.FieldDelete.as_view(), name='fields_delete'),
    
    # Add a dino to a specific field
    path('fields/<int:field_id>/add_dino/', views.add_dino, name='add_dino'),
    
    # Dino detail page with a specific dino's details
    path('dinos/<int:dino_id>/', views.dinos_detail, name='dinos_detail'),
    
    # Update a dino's information using its primary key
    path('Dinos/<int:pk>/update/', views.DinoUpdate.as_view(), name='dinos_update'),
    
    # Delete a dino using its primary key
    path('Dinos/<int:pk>/delete/', views.DinoDelete.as_view(), name='dinos_delete'),
    
    # Associate an animation with a dino
    path('dinos/<int:dino_id>/assoc_animation/', views.assoc_animation, name='assoc_animation'),
    
    # URL patterns for authentication (login, logout)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # User signup page
    path('accounts/signup/', views.signup, name='signup'),
]
