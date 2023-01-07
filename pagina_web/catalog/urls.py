from django.urls import re_path as url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<pk>', views.DirectorView.as_view(), name='director_detail'),
    path('templates/<pk>', views.FilmView.as_view(), name='film_detail')
]