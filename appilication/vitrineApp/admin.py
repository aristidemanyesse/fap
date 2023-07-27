from django.db import models
from django.db.models import  Q
from coreApp.models import BaseModel, Etat



class Jour(BaseModel):
    name    = models.CharField(max_length = 255, null = True, blank=True)

    class Meta:
        ordering = ['name']


class Event(BaseModel):
    jour     = models.ForeignKey(Jour, on_delete = models.CASCADE, null = True, blank=True, related_name="categorie_produit")
    name          = models.CharField(max_length = 255, default="", null = True, blank=True)
    heure          = models.TimeField(null = True, blank=True)
    description   = models.TextField(default = "")
    image1        = models.ImageField(max_length = 255, upload_to = "media/images/produits/", default='media/images/produits/default.png', null = True, blank=True)
    image2        = models.ImageField(max_length = 255, upload_to = "media/images/produits/", default='media/images/produits/default.png', null = True, blank=True)
    image3        = models.ImageField(max_length = 255, upload_to = "media/images/produits/", default='media/images/produits/default.png', null = True, blank=True)
    
    class Meta:
        ordering = ['name']



class TypeParticipant(BaseModel):
    type    = models.CharField(max_length = 255, null = True, blank=True)

        
class Participant(BaseModel):
    name     = models.CharField(max_length = 255, default="", null = True, blank=True)
    fonction = models.TextField(default = "")
    type     = models.ForeignKey(TypeParticipant, on_delete = models.CASCADE, null = True, blank=True, related_name="type_participant")
    image    = models.ImageField(max_length = 255, upload_to = "media/images/participants/", default='media/images/participants/default.png', null = True, blank=True)
    email    = models.EmailField(null = True, blank=True)
    contact  = models.CharField(max_length = 255, default="", null = True, blank=True)
    adreese  = models.CharField(max_length = 255, default="", null = True, blank=True)
    
    class Meta:
        ordering = ['name']



class Activity(BaseModel):
    title       = models.CharField(max_length = 255, default="", null = True, blank=True)
    subtitle    = models.CharField(max_length = 255, default="", null = True, blank=True)
    description = models.TextField(default = "")
    image1      = models.ImageField(max_length = 255, upload_to = "media/images/produits/", default='media/images/produits/default.png', null = True, blank=True)
    image2      = models.ImageField(max_length = 255, upload_to = "media/images/produits/", default='media/images/produits/default.png', null = True, blank=True)
    image3      = models.ImageField(max_length = 255, upload_to = "media/images/produits/", default='media/images/produits/default.png', null = True, blank=True)
