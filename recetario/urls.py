from django.urls import path
from . import views

urlpatterns = [
   
    path('nueva_receta', views.RecetaView.as_view(), name="nueva-receta"),
    path('thank_u', views.ThankYouView.as_view(), name="thank-u"),
    path('', views.RecetaListView.as_view(), name="recetas-list"),
    path('recetas/<int:pk>', views.SingleRecetaView.as_view(), name="single-receta"),
    path('delete/<int:pk>', views.RecetaDeleteView.as_view(), name="delete-receta"),
    path('update/<int:pk>', views.RecetaUpdateView.as_view(), name="update-receta")
]