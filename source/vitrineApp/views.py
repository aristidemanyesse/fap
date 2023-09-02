from django.shortcuts import render
from annoying.decorators import render_to

# Create your views here.


@render_to('vitrineApp/index.html')
def main(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    

@render_to('vitrineApp/mna.html')
def mna(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    

@render_to('vitrineApp/fap.html')
def fap(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    

@render_to('vitrineApp/afc.html')
def afc(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    

@render_to('vitrineApp/fwa.html')
def fwa(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('vitrineApp/billetterie.html')
def billetterie(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('vitrineApp/participants.html')
def danse(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('vitrineApp/participants.html')
def fica(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('vitrineApp/stand.html')
def stand(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
# @render_to('vitrineApp/unes.html')
# def unes(request):
#     if request.method == "GET":
#         ctx = {}
#         return ctx
    
    
@render_to('vitrineApp/contacts.html')
def contacts(request):
    if request.method == "GET":
        ctx = {}
        return ctx