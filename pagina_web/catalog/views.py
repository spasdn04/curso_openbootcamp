from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Author, Genre, Film

def index(request):
    authors = Author.objects.all()
    films = Film.objects.all()
    genres = Genre.objects.all()
    
    return render(
        request,
        'index.html',
        context={
            'authors':authors,
            'films':films,
            'genres':genres
        }
    )

class DirectorView(generic.DetailView):
    template_name = 'authors.html'
    model = Author
    
class FilmView(generic.DeleteView):
    template_name = 'films.html'
    model = Film