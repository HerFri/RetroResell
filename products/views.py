from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # OR logic
from django.db.models.functions import Lower

from .models import Product, Platform, Category, Comment
from .forms import ProductForm, CommentForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    platforms = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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

    current_sorting = f'{sort}_{direction}'	

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_platforms': platforms,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details and 
    for posting comments"on indivisual products """

    product = get_object_or_404(Product, pk=product_id)
    comments = product.comments.filter(approved=True).order_by('created_on')

    context = {
        'product': product,
        'comment_form': CommentForm(),
        'comments': comments,
        'commented': False,
    }

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.product = product
            comment.author = request.user
            comment.save()
            context = {
                'product': product,
                'commented': True,
                'comment_form': CommentForm(),
                'comments': comments,
            }
            return render(request, 'products/product_detail.html', context)
        else:
            comment_form = CommentForm()    
    return render(request, 'products/product_detail.html', context)

@login_required
def edit_comment(request, comment_id):
    """
    Allows authenticated users to edit a comment
    """
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, f'Comment has been edited!')
            return redirect('product_detail', product_id=comment.product.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'products/edit_comment.html', {'form': form,
                  'comment': comment})


@login_required
def delete_comment(request, comment_id):
    """
    Allows authenticated users to delete a comment
    """
    if (request.user.is_superuser):
        comment = get_object_or_404(Comment, pk=comment_id)
    else:
        comment = get_object_or_404(Comment, pk=comment_id,
                                    author=request.user)
    if request.user.is_superuser or request.user == comment.author:
        if request.method == 'POST':
            comment.delete()
            messages.success(request, f'Comment deleted successfully!')
            return redirect('product_detail', product_id=comment.product.pk)
        return render(request, 'products/delete_comment.html', {'comment': comment})
    else:

        return redirect('product_detail', product_id=comment.product.pk)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
   
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
