from django.db import models
from django.urls import reverse

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=64, help_text='Nombre del género')
    
    def __str__(self):
        return self.name
    
class Film(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    summary = models.TextField(max_length=300, help_text='Descripcion')
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("film-detail", kwargs={"pk": self.pk})

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    