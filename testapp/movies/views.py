from django.shortcuts import render
# Create your views here.
from django.views.decorators.cache import cache_page
from testapp.settings import CACHE_TTL
from movies.api import MovieAPI as api

@cache_page(CACHE_TTL)
def index(request):         
    context = {'data': api.get_movie_data()}
    return render(request, 'movies/index.html', context)

