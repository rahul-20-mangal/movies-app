from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie


class MovieListView(ListView):
    model = Movie
