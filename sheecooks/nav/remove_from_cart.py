from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from.forms import PaymentForm
from collections import Counter
from django.db.models import Count
from .models import Product,Splice_display,Cart, checkout_information
from .views import add_items_tocart

@login_required
def remove_items_from_cart(request):
    if request.method == "POST":
        food_id = request.POST.get('remove_id')
        food_name = request.POST.get('remove_name')
        try:
            menu_item = Cart.objects.filter(cart_product_id__product_serial_no = food_id)

        except Cart.DoesNotExist:
            return redirect('view_cart_items')
        #item_to_remove = menu_item
        menu_item.delete()
        messages.success(request, 'Item removed from cart.')
    return HttpResponseRedirect ("view_cart_items")

@login_required
def reduce_cart_item_by_one (request):
    user = request.user
    id_to_remove = request.POST.get('minus_id')
    # menu_items_in_cart = Cart.objects.filter(user_id=user).values('cart_product_id__product_name','cart_product_id__product_selling_price', 'cart_product_id__photo','cart_product_id__product_serial_no' ).annotate(number_items=Count('cart_product_id'))
    if request.method =='POST':
        food_to_remove = Cart.objects.filter(cart_product_id__product_serial_no = id_to_remove).order_by('id')
        item_to_delete = food_to_remove.first()
        item_to_delete.delete()
    return HttpResponseRedirect ("view_cart_items")

@login_required
def add_one_item_tocart (request):
    if request.method =='POST':
        food_to_add = request.POST.get('add_id')
        user = request.user

    try:
        item_to_add = Product.objects.get(product_serial_no = food_to_add)

    except Product.DoesNotExist:
        return redirect('add_items_tocart')

    menucart_item = Cart(user_id = request.user, cart_product_id = item_to_add)
    menucart_item.save()
    messages.success(request, 'Item added to cart.')
    return HttpResponseRedirect ("view_cart_items")