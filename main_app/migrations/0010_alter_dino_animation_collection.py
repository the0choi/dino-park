# Generated by Django 4.2.4 on 2023-08-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_rename_dino_animation_dino_colour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dino',
            name='animation_collection',
            field=models.ManyToManyField(related_name='dinos', to='main_app.animation'),
        ),
    ]