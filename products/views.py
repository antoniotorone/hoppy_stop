from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


# create your view here


def all_products(request):
    """A view that show all products and includes sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
               
                messages.error(request, "No results matched your query")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(taste__icontains=query) | Q(style__icontains=query)
            products = products.filter(queries)
        if not products:
              messages.error(request, "No results matched your query")
              return redirect(reverse('products'))


    context = {
        'products': products,
        'search_query': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view that show a single product """

    product = get_object_or_404(Product, pk=product_id)
    review = Review.objects.filter(product=product)
   

    context = {
        'review': review,
        'product': product,

    }
    
    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ The shop owner can add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry this functionality is only for the store owners')
        return redirect(reverse('home'))
        
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product successfully added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please check your form and try again')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context) 

@login_required
def edit_product(request, product_id):
    """ Edit a product"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry this functionality is only for the store owners')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated with success')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to edit a product. Please check your form and try again')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing { product.name }')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ delete a product"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry this functionality is only for the store owners')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))


def add_review(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=id)
        user = request.user 
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                form = form.save(commit=False)
                form.product = product
                form.user = user
                form.save()
                messages.success(request, 'Review left with success ')
            return redirect(reverse('product_detail', args=[product.id]))