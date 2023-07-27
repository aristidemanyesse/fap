from django.urls import path

from . import views

app_name = "vitrineApp"
urlpatterns = [
    path('', views.main, name='main'),
    path('programme', views.programme, name='programme'),
    path('participants', views.participants, name='participants'),
    path('stand', views.stand, name='stand'),
]