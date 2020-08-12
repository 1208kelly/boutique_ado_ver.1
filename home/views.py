from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def index(request):
    """ A view to return the index page """
    messages.error(request, "There's nothing in your bag at the moment")
    return render(request, 'home/index.html')