# Generated by Django 3.1.14 on 2022-06-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20220623_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='defence',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='health',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='level',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='stamina',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='strength',
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(default=5),
        ),
    ]
