from django.urls import path
from . import views

app_name = 'directors'

urlpatterns = [
    path('', views.DirectorListView.as_view(), name='list'),
]