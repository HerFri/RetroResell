from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q  # OR logic
from .models import Product, Platform

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    platform = None

    if request.GET:
        if 'platform' in request.GET:
            platforms = request.GET['platform'].split(',')
            products = products.filter(platform__name__in=platforms)
            platforms = Platform.objects.filter(name__in=platforms)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(genre__icontains=query) | Q(platform__name__icontains=query) # i = makes queries case insensitive
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_platforms': platforms,
    }

    
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    
    return render(request, 'products/product_detail.html', context)