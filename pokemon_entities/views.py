import folium
import json

from django.utils.timezone import localtime
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity



MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    existing_pokemons = PokemonEntity.objects.filter(disappeared_at__gte=localtime()).filter(appeared_at__lte=localtime())
    for pokemon_entity in existing_pokemons:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.image.url),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        requested_pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        raise HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    pokemon_entities = PokemonEntity.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    image_url = request.build_absolute_uri(requested_pokemon.image.url)

    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            image_url)

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': {'img_url': image_url,
                    'title_ru': requested_pokemon.title,
                    'title_en': requested_pokemon.title_en,
                    'title_jp': requested_pokemon.title_jp,
                    'description': requested_pokemon.description}
    })
