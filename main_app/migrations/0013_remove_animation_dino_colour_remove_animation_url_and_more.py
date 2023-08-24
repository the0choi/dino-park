# Generated by Django 4.2.4 on 2023-08-24 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_field_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animation',
            name='dino_colour',
        ),
        migrations.RemoveField(
            model_name='animation',
            name='url',
        ),
        migrations.RemoveField(
            model_name='dino',
            name='animation_collection',
        ),
        migrations.AddField(
            model_name='dino',
            name='animations',
            field=models.ManyToManyField(to='main_app.animation'),
        ),
        migrations.AlterField(
            model_name='animation',
            name='action',
            field=models.CharField(choices=[('Idle', 'Idle'), ('Move', 'Move'), ('Kick', 'Kick'), ('Hurt', 'Hurt'), ('Dash', 'Dash'), ('Bite', 'Bite'), ('Dead', 'Dead'), ('Jump', 'Jump'), ('Avoid', 'Avoid')], max_length=20),
        ),
    ]
