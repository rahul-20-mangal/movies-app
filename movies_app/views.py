from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Movie, Genre, Studio, Director


class MovieListView(ListView):
    model = Movie


def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    context = {
        'movie': movie
    }
    return render(request, 'movies_app/movie_detail.html', context=context)


def genre_list(request):
    genre_list = Genre.objects.all()

    context = {
        'genre_list': genre_list 
    }
    return render(request, 'movies_app/genre_list.html', context=context)


def genre_detail(request, slug):
    genre = get_object_or_404(Genre, slug=slug)

    context = {
        'genre': genre
    }
    return render(request, 'movies_app/genre_detail.html', context=context)


class StudioListView(ListView):
    model = Studio


class StudioDetailView(DetailView):
    model = Studio


class DirectorListView(ListView):
    model = Director