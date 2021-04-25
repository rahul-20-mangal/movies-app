from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Movie


class MovieListView(ListView):
    model = Movie


def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    context = {
        'movie': movie
    }
    return render(request, 'movies_app/movie_detail.html', context=context)
