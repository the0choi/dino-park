from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import random

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

ACTIONS = (
    ('IDLE', 'Idle'),
    ('MOVE', 'Move'),
    ('KICK', 'Kick'),
    ('HURT', 'Hurt'),
    ('DASH', 'Dash'),
    ('BITE', 'Bite'),
    ('DEAD', 'dead'),
    ('JUMP', 'Jump'),

)

class Field(models.Model):
    date = models.DateField('Date', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_dinos(self):
        return Dino.objects.filter(field=self)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def __str__(self):
        return f'{self.date} ({self.id})'

    def get_absolute_url(self):
        return reverse('fields_detail', kwargs={'field_id': self.id})

class Animation(models.Model):
    action = models.CharField(max_length=50)
    url = models.URLField()
    dino_colour = models.ForeignKey('Dino', on_delete=models.CASCADE, related_name='animations')

    def __str__(self):
        return self.get_action_display()

class Dino(models.Model):
    name = models.CharField(
        max_length=20,
        default="Dino"
    )
    colour = models.CharField(
        choices=COLOURS,
        default=1
    )
    duration = models.CharField(max_length=20)
    url = models.URLField(max_length=200)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    animation_collection = models.ManyToManyField('Animation', related_name='dinos')

    def __str__(self):
        return f'{self.duration} ({self.id})'

    def get_absolute_url(self):
        return reverse('dinos_detail', kwargs={'dino_id': self.id})


