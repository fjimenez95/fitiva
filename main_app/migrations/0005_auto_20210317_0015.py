# Generated by Django 3.1.7 on 2021-03-17 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210317_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_type',
            field=models.CharField(choices=[('a', 'run'), ('b', 'ride'), ('c', 'walk'), ('g', 'hike'), ('h', 'canoe'), ('i', 'weight training'), ('j', 'swim'), ('k', 'cross-fit'), ('l', 'stairs-stepper'), ('m', 'elliptical'), ('n', 'workout - other')], default='run', max_length=50),
        ),
    ]