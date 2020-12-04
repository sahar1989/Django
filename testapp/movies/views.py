from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import requests

""" global variables """
_base_url = 'https://ghibliapi.herokuapp.com/'
FILMS='films'
PEOPLE='people'

def parse_films(film):
    """ extract id, title and create people object field to be fill later """
    return {
        'id': film.get('id'),
        'title': film.get('title'),
        'people':[]
    }
    
def extract_id_from_url(film):
    """ film id is a url then just extract the id exp: https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6 """
    return film.split('/')[-1]
    
def parse_peoples(peoples):
    """extract name, films from people"""
    return {
        'name': peoples.get('name'),
        'films_id': [
            extract_id_from_url(film) 
            for film in peoples.get('films')
        ],
    }

def index(request):
    """ get films date from url api """ 
    films_data = requests.get(_base_url+FILMS).json()
    films = [parse_films(film) for film in films_data]
    """ get people data from url api """
    people_data = requests.get(_base_url+PEOPLE).json()
    people = [parse_peoples(p) for p in people_data]
    
    final_data = films.copy() 
    """ bind people and film """
    for p in people:
          for p_film_id in p['films_id']:
            for film in final_data:
                if p_film_id == film['id']:
                    film['people'].append(p['name'])
           
    """ return data to template """           
    context = {'data': final_data}
    return render(request, 'movies/index.html', context)
