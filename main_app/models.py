from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Available color options for dino
COLOURS = (
    ('Blue', 'Blue'),
    ('Pink', 'Pink'),
    ('Grey', 'Grey'),
    ('Dark Blue', 'Dark Blue'),
    ('Light Grey', 'Light Grey'),
    ('Red', 'Red'),
    ('Orange', 'Orange'),
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Dark Green', 'Dark Green')
)

# Available actions/animations for dino
ACTIONS = (
    ('Move', 'Move'),
    ('Kick', 'Kick'),
    ('Dance', 'Dance'),
    ('Jump', 'Jump'),
)

# Represents the field where dinos are hatched
class Field(models.Model):
    date = models.DateField('Date')  # Date of the field
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User associated with the field
    duration = models.CharField(default='0')  # Duration of the field's session

    def get_dinos(self):
        return Dino.objects.filter(field=self)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def __str__(self):
        return f'{self.date} ({self.id})'

    def get_absolute_url(self):
        return reverse('fields_detail', kwargs={'field_id': self.id})

# Represents different animations that can be assigned to dino
class Animation(models.Model):
    action = models.CharField(
        max_length=20,
        choices=ACTIONS
    )

    def __str__(self):
        return self.action

# Represents a dino entity with attributes and animations
class Dino(models.Model):
    name = models.CharField(
        max_length=20,
        default="Dino"
    )
    colour = models.CharField(
        choices=COLOURS,
        default=1
    )
    duration = models.CharField(max_length=20)  # Duration of the dino's session
    url = models.URLField(max_length=200)  # URL associated with the dino
    field = models.ForeignKey(Field, on_delete=models.CASCADE)  # Field in which the dinos is present
    
    # Assignable animations for the dino
    animations = models.ManyToManyField(Animation)

    def __str__(self):
        return f'{self.duration} ({self.id})'

    def get_absolute_url(self):
        return reverse('dinos_detail', kwargs={'dino_id': self.id})
