from django.shortcuts import render, redirect
from .models import Product, CartItem

# Create your views here.
def products(request):
    """
    This view function retrieves all products from the database and renders them to the 'products/products.html' template.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered template response.
    """
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products':products})


def add_to_cart(request, product_id):
    """
    This view function handles adding a product to the user's cart.

    Args:
        request (HttpRequest): The incoming HTTP request.
        product_id (int): The ID of the product to add.

    Returns:
        HttpResponse: The rendered template response.
    """
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    cart_items = CartItem.objects.filter(user=request.user)
    
    # Calculate the total price of all items in the cart
    for item in cart_items:
        item.total_price = item.quantity * item.product.price
    total_price = sum(item.total_price for item in cart_items)

    return render(request, 'products/cart.html', {
        'success_message': 'Item has successfully been added to cart.',
        'cart_items': cart_items,
        'total_price': total_price,
    })


def view_cart(request):
    """
    This view function displays the user's cart items and the total price.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered template response.
    """
    cart_items = CartItem.objects.filter(user=request.user)
    
    # Calculate the total price of all items in the cart
    for item in cart_items:
        item.total_price = item.quantity * item.product.price
    total_price = sum(item.total_price for item in cart_items)

    return render(request, 'products/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def clear_cart(request):
    """
    This view function clears the user's cart.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered template response.
    """
    cart_items = CartItem.objects.filter(user=request.user)
    cart_items.delete()
    context = {'success_message': 'Cart has been successfully cleared.'}
    return render(request, 'products/cart.html', context)
