from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HFJ2aLlcEoQaMZcsfp8PQwgauFZY0PmdYawEJHXb0FscfgglNB7XqAFaxt1j0gCqmVHa1ACvtZXszbrbT3psmDg00LdPYPONk'
    }

    return render(request, template, context)
