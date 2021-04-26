from django.urls import path
from . import views

app_name = 'studios'

urlpatterns = [
    path('', views.StudioListView.as_view(), name='list'),
    path('<slug:slug>/', views.StudioDetailView.as_view(), name='detail'),
]