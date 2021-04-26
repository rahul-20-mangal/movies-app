from django.urls import path
from . import views

app_name = 'studios'

urlpatterns = [
    path('', views.StudioListView.as_view(), name='list'),
]