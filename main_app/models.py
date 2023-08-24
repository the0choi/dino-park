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
    ('Move', 'Move'),
    ('Kick', 'Kick'),
    ('Dance', 'Dance'),
    ('Jump', 'Jump'),
)


class Field(models.Model):
    date = models.DateField('Date', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.CharField(default='0')

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
    action = models.CharField(
        max_length=20,
        choices=ACTIONS
    )

    def __str__(self):
        return self.action


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
    animations = models.ManyToManyField(Animation)

    def __str__(self):
        return f'{self.duration} ({self.id})'

    def get_absolute_url(self):
        return reverse('dinos_detail', kwargs={'dino_id': self.id})
