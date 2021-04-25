from django.contrib import admin
from movies_app.models import Movie, Director, Studio, Genre, Review

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Studio)
admin.site.register(Genre)
admin.site.register(Review)
