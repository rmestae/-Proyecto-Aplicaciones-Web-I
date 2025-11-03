from django.db import models

class Receta(models.Model):
    nombre_receta = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)
    utensilios = models.TextField(max_length=2000)
    ingredientes = models.TextField(max_length=8000)
    procedimiento = models.TextField(max_length=8000)
    image = models.ImageField(upload_to='recetas', null=True)

    def __str__(self):
        return f"ID:{self.pk} {self.nombre_receta.title()} "



# Create your models here.
