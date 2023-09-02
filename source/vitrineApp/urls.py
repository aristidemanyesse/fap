from django.urls import path

from . import views

app_name = "vitrineApp"
urlpatterns = [
    path('', views.main, name='main'),
    path('foire-africaine-de-paris/', views.fap, name='fap'),
    path('marche-de-noel-africain/', views.mna, name='mna'),
    path('african-fashion-cook/', views.afc, name='afc'),
    path('fashion-west-africa/', views.fwa, name='fwa'),
    path('billetterie/', views.billetterie, name='billetterie'),
    path('danse/', views.danse, name='danse'),
    path('fica/', views.fica, name='fica'),
    # path('programme', views.programme, name='programme'),
    # path('participants', views.participants, name='participants'),
    path('stand/', views.stand, name='stand'),
    # path('unes', views.unes, name='unes'),
    path('contacts/', views.contacts, name='contacts'),
]