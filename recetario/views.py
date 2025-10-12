from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
recetas = {
    "Receta 1" : "proximamente 1",
    "Receta 2" : "proximamente 2",
    "Receta 3" : "proximamente 3"
}

def index(request):
    
    recetas_count = len(recetas)

    recetas_list = list(recetas.keys())

    return render(request, 'recetario/home.html', {
        "recetas" : recetas_count,
        "recetas_list" : recetas_list,
    })

def receta(request, name):
    try:
        receta_text = recetas[name]
        return render(request,
                      'recetario/receta.html',
                      {
                          "receta_name" : name,
                          "receta_text" : receta_text,
                      })
    
    except:
        return HttpResponseNotFound("No encontré la receta "+ name)
    
