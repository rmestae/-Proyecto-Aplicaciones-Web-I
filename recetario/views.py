from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .recetas_data import recetas

from .models import Receta
from .forms import RecetaForm, RecetaUpdateForm

from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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
    

class RecetaView(CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = "recetario/nueva_receta.html"
    success_url = "thank_u"

class ThankYouView(TemplateView):
    template_name = "recetario/thank_u.html"

    
class RecetaListView(ListView):
    template_name = "recetario/recetas_list.html"
    model = Receta
    context_object_name = "recetas_list"

class SingleRecetaView(DetailView):
    template_name = "recetario/receta.html"
    model = Receta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        receta_actual = self.object

        utensilios_input = receta_actual.utensilios
        ingredientes_input = receta_actual.ingredientes
        procedimiento_input = receta_actual.procedimiento

        context["utensilios"] = [item.strip() for item in utensilios_input.split(',') if item.strip()]
        context["ingredientes"] = [item.strip() for item in ingredientes_input.split(',') if item.strip()]
        context["procedimiento"] = [item.strip() for item in procedimiento_input.split('/') if item.strip()]

        return context
    
class RecetaDeleteView(DeleteView):
    model = Receta
    success_url = "/recetario/thank_u"
    template_name = "recetario/confirm_delete.html"

class RecetaUpdateView(UpdateView):
    model = Receta
    form_class = RecetaUpdateForm
    template_name = "recetario/update_receta.html"
    success_url = "/recetario/thank_u"
        
