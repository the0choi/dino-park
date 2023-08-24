# Generated by Django 4.2.4 on 2023-08-24 02:02

from django.db import migrations
from main_app.models import Animation

def populate_animations(apps, schema_editor):
    Animation = apps.get_model('main_app', 'Animation')
    animations_data = [
        {"action": "Move"}, 
        {"action": "Kick"}, 
        {"action": "Hurt"}, 
        {"action": "Dash"}, 
        {"action": "Bite"}, 
        {"action": "Dead"}, 
        {"action": "Jump"}, 
        {"action": "Avoid"},
    ]
    for animation_data in animations_data:
        Animation.objects.create(**animation_data)

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20230824_0201'),
    ]

    operations = [
        migrations.RunPython(populate_animations),
    ]
