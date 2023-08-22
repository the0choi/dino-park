from django.forms import ModelForm
from .models import Dino

class DinoForm(ModelForm):
  class Meta:
    model = Dino
    fields = ['name', 'colour', 'duration']
