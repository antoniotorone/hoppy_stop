from django.shortcuts import render
from .models import Product

#create your view here


def all_products(request):
    """A view that show all products and includes sorting and search queries"""

    products = Product.objects.all()

    context = {
        'products' : products,
    }
    
    return render(request, 'products/products.html', context)
