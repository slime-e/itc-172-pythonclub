from .models import ProductType, Product, Review
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index (request):
    return render(request, 'club/index.html')


def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'club/types.html' ,{'type_list' : type_list})


def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'club/products.html', {'products_list': products_list})


def productdetails(request, id):
    prod = get_object_or_404(Product, pk=id)
    discount=prod.memberdiscount
    reviews = Review.objects.filter(product=id).count()
    context={
        'prod' : prod,
        'discount' : discount,
        'reviews' : reviews,
    }
    return render(request, 'club/proddetails.html', context=context)