from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_basket(request):
    """This view render the basket page"""

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add the quantity of the specified item to the basket"""
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    print(quantity)
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)

# UPDATE THE BASKET
def adapt_basket(request, item_id):
    """ Adabt the quantity and the amount of the specified item to the basket"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
    else:
        basket.pop[item_id]
        messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

#REMOVE FROM THE BASKET
def remove_from_basket(request, item_id):
    """ Remove the specified item from the basket"""
    product = get_object_or_404(Product, pk=item_id)
    basket = request.session.get('basket', {})
    try:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)
       

    except Exception as e:
        messages.error(request, f'Error removing item:{e}')
        return HttpResponse(status=500)
