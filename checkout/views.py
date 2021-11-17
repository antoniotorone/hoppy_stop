from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import  basket_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "No items in you basket ")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    gross = current_basket['grand_total']
    stripe_total = round(gross * 100)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ja0RlKv883G0Cvh4A7pOnUtHWi4q4X2LHShTdLHTjNfjbdYACn7CUDH3QzBCCDp3KYrgFn8oJ6tIXv1jPCjwKLM00HbVrgj3u',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)



