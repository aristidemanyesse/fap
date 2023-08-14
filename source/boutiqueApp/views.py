from django.shortcuts import render
from annoying.decorators import render_to

# Create your views here.


@render_to('boutiqueApp/index.html')
def main(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('boutiqueApp/produit.html')
def produit(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    