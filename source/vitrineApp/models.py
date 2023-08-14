from django.db import models
from django.db.models import  Q
from coreApp.models import BaseModel, Etat



class Edition(BaseModel):
    name    = models.CharField(max_length = 255, null = True, blank=True)



class TypeParticipant(BaseModel):
    name        = models.CharField(max_length = 255, null = True, blank=True)
    etiquette   = models.CharField(max_length = 255, null = True, blank=True)



class Jour(BaseModel):
    name    = models.CharField(max_length = 255, null = True, blank=True)
    edition = models.ForeignKey(Edition, on_delete = models.CASCADE, null = True, blank=True, related_name="edition_jour")


class Participant(BaseModel):
    fullname    = models.CharField(max_length = 255, default="", null = True, blank=True)
    fonction    = models.CharField(max_length = 255, default="", null = True, blank=True)
    photo       = models.ImageField(max_length = 255, upload_to = "media/images/participants/", default='media/images/participants/default.png', null = True, blank=True)
    type        = models.ForeignKey(TypeParticipant, on_delete = models.CASCADE, null = True, blank=True, related_name="type_participant")
    email       = models.EmailField(null = True, blank=True)
    contact     = models.CharField(max_length = 255, default="", null = True, blank=True)


class Actualite(BaseModel):
    titre         = models.CharField(max_length = 255, default="", null = True, blank=True)
    paragraphe1   = models.TextField(default = "")
    paragraphe2   = models.TextField(default = "")
    paragraphe3   = models.TextField(default = "")
    image1        = models.ImageField(max_length = 255, upload_to = "media/images/actualites/", default='media/images/actualites/default.png', null = True, blank=True)
    image2        = models.ImageField(max_length = 255, upload_to = "media/images/actualites/", default='media/images/actualites/default.png', null = True, blank=True)
    image3        = models.ImageField(max_length = 255, upload_to = "media/images/actualites/", default='media/images/actualites/default.png', null = True, blank=True)
    image4        = models.ImageField(max_length = 255, upload_to = "media/images/actualites/", default='media/images/actualites/default.png', null = True, blank=True)
    jour       = models.ForeignKey(Edition, on_delete = models.CASCADE, null = True, blank=True, related_name="jour_actualite")
    


class Evenement(BaseModel):
    jour          = models.ForeignKey(Jour, on_delete = models.CASCADE, null = True, blank=True, related_name="categorie_produit")
    name          = models.CharField(max_length = 255, default="", null = True, blank=True)
    date          = models.DateTimeField(null = True, blank=True)
    description   = models.TextField(default = "")
    image1        = models.ImageField(max_length = 255, upload_to = "media/images/events/", default='media/images/events/default.png', null = True, blank=True)
    image2        = models.ImageField(max_length = 255, upload_to = "media/images/events/", default='media/images/events/default.png', null = True, blank=True)
    image3        = models.ImageField(max_length = 255, upload_to = "media/images/events/", default='media/images/events/default.png', null = True, blank=True)
    
    

class CategorieStand(BaseModel):
    name          = models.CharField(max_length = 255, default="", null = True, blank=True)



class Stand(BaseModel):
    name        = models.CharField(max_length = 255, default="", null = True, blank=True)
    date        = models.DateTimeField(null = True, blank=True)
    email       = models.EmailField(null = True, blank=True)
    contact     = models.CharField(max_length = 255, default="")
    contact2    = models.CharField(max_length = 255, default="")
    description = models.TextField(default = "")
    categorie   = models.ForeignKey(CategorieStand, on_delete = models.CASCADE, null = True, blank=True, related_name="categorie_stand")
    edition     = models.ForeignKey(Jour, on_delete = models.CASCADE, null = True, blank=True, related_name="edition_stand")