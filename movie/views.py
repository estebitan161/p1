from django.shortcuts import render
from .models import Movie 

# Create your views here.

def home(request):
    # Obtener el término de búsqueda desde el parámetro GET de la URL
    searchTerm = request.GET.get('searchMovie', '')

    if searchTerm:
        # Filtrar las películas cuyo título contenga el término de búsqueda, sin distinguir mayúsculas y minúsculas
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        # Si no se ingresa ningún término de búsqueda, devolver todas las películas
        movies = Movie.objects.all()

    # Renderizar la plantilla 'home.html' con el contexto de las películas y el término de búsqueda
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies, 'name':'Esteban Villa Parra'})


def about(request):
    #return HttpResponse('<h1>Welcome to about Page</h1>')
    return render(request, 'about.html', {'name':'Esteban Villa Parra'})