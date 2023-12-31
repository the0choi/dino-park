# Generated by Django 4.2.4 on 2023-08-23 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_dino_colour_alter_dino_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('dino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animations', to='main_app.dino')),
            ],
        ),
        migrations.AddField(
            model_name='dino',
            name='animation_collection',
            field=models.ManyToManyField(related_name='dinos', to='main_app.animation'),
        ),
    ]
