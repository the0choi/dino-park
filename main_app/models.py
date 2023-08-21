from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Field(models.Model):
    date = models.DateField('Date', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def __str__(self):
        return f'{self.date} ({self.id})'

    def get_absolute_url(self):
        return reverse('fields_detail', kwargs={'field_id': self.id})


class Dino(models.Model):
    name = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    url = models.URLField(max_length=200)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.duration} ({self.id})'

    def get_absolute_url(self):
        return reverse('dinos_detail', kwargs={'dino_id': self.id})
