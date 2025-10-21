from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .recetas_data import recetas

# Create your views here.

def index(request):
    
    recetas_count = len(recetas)
    recetas_list = (sorted(recetas.items()))

    return render(request, 'recetario/home.html', {
        "recetas" : recetas_count,
        "recetas_list" : recetas_list,
    })

def receta(request, name):
    try:
        receta_text = recetas[name]['descripcion']
        tiempo = recetas[name]['tiempo']
        utensilios = list(recetas[name]['utensilios'])
        ingredientes = list(recetas[name]['ingredientes'])
        procedimiento = list(recetas[name]['procedimiento'])
        return render(request,
                      'recetario/receta.html',
                      {
                          "receta_name" : name,
                          "receta_text" : receta_text,
                          "tiempo" : tiempo,
                          "utensilios" : utensilios,
                          "ingredientes" : ingredientes,
                          "procedimiento" : procedimiento,
                      })
    
    except:
        return HttpResponseNotFound("No encontré la receta "+ name)
    
