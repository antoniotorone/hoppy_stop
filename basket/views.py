from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """This view render the basket page"""

    return render(request, 'basket/basket.html')
