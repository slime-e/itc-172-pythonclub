from .models import ProductType, Product, Review
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'club/index.html')


def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'club/types.html' ,{'type_list' : type_list})


