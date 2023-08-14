from django.urls import path

from . import views

app_name = "boutiqueApp"
urlpatterns = [
    path('', views.main, name='main'),
    path('produit', views.produit, name='produit'),
]