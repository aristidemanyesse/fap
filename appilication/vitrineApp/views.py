from django.shortcuts import render
from annoying.decorators import render_to

# Create your views here.


@render_to('vitrineApp/index.html')
def main(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('vitrineApp/programme.html')
def programme(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('vitrineApp/participants.html')
def participants(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('vitrineApp/stand.html')
def stand(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('vitrineApp/unes.html')
def unes(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('vitrineApp/contacts.html')
def contacts(request):
    if request.method == "GET":
        ctx = {}
        return ctx