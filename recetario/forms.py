from .models import Receta
from django import forms

class RecetaForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Receta
        fields = "__all__"
        labels = {
            "nombre_receta" : "Nombre Receta",
            "descripcion" : "Descripción",
            "utensilios": "Utensilios",
            "ingredientes" : "Ingredientes",
            "procedimiento" : "Procedimiento",
            "image" : "Imagen"
        }

class RecetaUpdateForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Receta
        fields = "__all__"
        exclude = ['nombre_receta']
        labels = {
            "descripcion" : "Descripción",
            "utensilios": "Utensilios",
            "ingredientes" : "Ingredientes",
            "procedimiento" : "Procedimiento",
            "image" : "Imagen"
        }