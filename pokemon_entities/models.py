from django.db import models  # noqa F401
from datetime import datetime


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя(русское)')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Имя(английское)')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Имя(японское)')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    element_type = models.ManyToManyField('PokemonElementType', related_name='element_types', verbose_name='Стихия')
    previous_evolution = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='next_evolutions',
        verbose_name='Из кого эволюционировал'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                verbose_name='Покемон',
                                related_name='entities')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(default=datetime.now, verbose_name='Появится')
    disappeared_at = models.DateTimeField(default=datetime.now, verbose_name='Исчезнет')
    level = models.IntegerField(blank=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, verbose_name='Сила')
    defence = models.IntegerField(blank=True, verbose_name='Защита')
    stamina = models.IntegerField(blank=True, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon.title}'


class PokemonElementType(models.Model):
    title = models.CharField(max_length=50, default=None, verbose_name='Тип стихии')

    def __str__(self):
        return self.title