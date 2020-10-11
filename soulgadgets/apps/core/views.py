from django.shortcuts import render

# Create your views here.
from apps.store.models import Product

def frontpage(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'frontpage.html', context)


def contact(request):
    return render(request, 'contact.html')
