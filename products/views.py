from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

#create your view here


def all_products(request):
    """A view that show all products and includes sorting and search queries"""

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No results matched your query")
                return redirect(reverse ('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(taste__icontains=query) | Q(style__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_query': query,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view that show a single product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

