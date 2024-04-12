from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Splice_display, Toppicks, CartItems_menu,CartItems_toppick,checkout_information
from.forms import PaymentForm
from collections import Counter
from django.db.models import Count



# Create your views here.
def nav (request):
    food_list = Product.objects.all()
    splice_images = Splice_display.objects.all()
    Top_food_picks = Toppicks.objects.all()


    # for vvv in Top_food_picks:
    #     ttt = type(vvv)
    #     v = 0

    template = loader.get_template("nav.html")
    context = {
        "food_list": food_list,
        "splice_images": splice_images,
        "Top_food_picks": Top_food_picks,
        }
    return HttpResponse(template.render(context, request))

def product_details(request):

    product_id = request.GET['product_serial_no'] #gets the id of the item from the users request.

    try:
        item = Product.objects.get(product_serial_no =product_id)

        template = loader.get_template("product_details.html")
    except Exception as e:
        # print(f"#EXCEPTION: {e}\n")
        item = None
        context = {
            "error":e
        }
        template = loader.get_template("exception.html")

    context = {
        #"food_list": food_list,
        #"splice_images": splice_images,
        #"Top_food_picks": Top_food_picks,
        "prod_sn": product_id,
        "food": item,
    }
    return HttpResponse(template.render(context, request))

def toppick(request):
    top_food_picks = Toppicks.objects.all()
    try:
        toppicks_id = request.GET['id']
        toppick_item = Toppicks.objects.get(id = toppicks_id)
        template = loader.get_template("toppick.html")
    except Exception as e:
        toppick_item = None
        template = loader.get_template("exception.html")


    context = {
        "Top_food_picks": top_food_picks,
        "pick_id":toppicks_id,
        "pick":toppick_item,
    }
    return HttpResponse(template.render(context, request))

#function to add items to cart when the add to cart button is clicked on the toppick items. The user needs to be logged in to add items to cart, hence the @loginrequired decorater.

@login_required
def toppick_cart(request):

    if request.method == 'POST':
        toppick_id = request.POST.get('pick_id')
        toppick_name = request.POST.get('pick_name')
        toppick_quantity = request.POST.get('quantity')
        try:
            toppick_product_id = Toppicks.objects.get(id=toppick_id)

        except Toppicks.DoesNotExist:
            return redirect('add_toppick_tocart')  
        
        toppick_cart_item = CartItems_toppick (cart_owner = request.user, toppick_cart_product = toppick_product_id, quantity = toppick_quantity)
        toppick_cart_item.save()
        messages.success(request, 'Item added to cart.')
        return HttpResponseRedirect ("/")

#this is the function for adding the rest of the menu items to cart.
@login_required
def CartItem_menu (request):

    if request.method == 'POST':
        menu_id = request.POST.get('food_id')
        menu_name = request.POST.get('food_name')
        quantity = request.POST.get ('quantity')

        try:
            menu_item = Product.objects.get(product_serial_no = menu_id)

        except Product.DoesNotExist:
            return redirect('add_menu_tocart')

        menucart_item = CartItems_menu (user_id = request.user, menu_product_id = menu_item, quantity = quantity)
        menucart_item.save()
        messages.success(request, 'Item added to cart.')
        return HttpResponseRedirect ("/")

    
#view to get the total count of items in the shopping cart and display it in the shopping cart
@login_required
def total_cartitems (request):
    if request.method == 'POST':
        user = request.user
        total_cartitems = CartItems.objects.filter(user=user).count()
        context = {
            'total_cartitems':total_cartitems

        }
    template = loader.get_template("base.html")
    return HttpResponse(template.render(context, request))

#this is the shopping cart items views associated with a specific logged in user.

@login_required
def view_cart_items (request):
    user = request.user

    # items_in_cart = Cart.objects.filter(user_id=user_id).values('item_id__name', 'item_id__cost').annotate(number_items=Count('item_id'))


    cart_toppick = CartItems_toppick.objects.filter(cart_owner = user).all()
    cart_menu = CartItems_menu.objects.filter(user_id = user).all()

    total_toppicks_incart = cart_toppick.count()
    total_menu_incart = cart_menu.count()
    aggregate_cart = total_toppicks_incart + total_menu_incart


    toppick_items_in_cart = CartItems_toppick.objects.filter(cart_owner=user).values('toppick_cart_product__pick_description', 'toppick_cart_product__pick_price','toppick_cart_product__pick_photo' ).annotate(number_items=Count('toppick_cart_product'))

    # for bbb in toppick_items_in_cart:
    #    ks = bbb.keys()
    #    nnn = list(ks)[0]
    #    ttt = type(nnn)
    #    vvv = bbb.values()
    #    vnn = list(vvv)[0]
    #    ttt2 = type(vnn)
    #    v = 0
    
    menu_items_in_cart = CartItems_menu.objects.filter(user_id=user).values('menu_product_id__product_name', 'menu_product_id__product_selling_price','menu_product_id__photo' ).annotate(number_items=Count('menu_product_id'))


    template = loader.get_template("cart_items.html")
    context = {
        "toppick_items_in_cart": toppick_items_in_cart,
        "menu_items_in_cart": menu_items_in_cart,
        "aggregate_cart": aggregate_cart,
    }
    return HttpResponse(template.render(context, request))
@login_required
def client_checkout(request):
    form = PaymentForm() 
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        template = loader.get_template('checkout.html')
        if form.is_valid():
            checkout_information.objects.create(
                user_id = request.user,
                delivery_address = form.cleaned_data['delivery_address'],
                Card_number = form.cleaned_data['card_number'],
                expiration_on_card = form.cleaned_data['expiry_date'],
                Security_Code=form.cleaned_data['cvc_number']
            )
            return HttpResponseRedirect ("/payment_success")
        else:
            form = PaymentForm()
        
    return render(request, 'checkout.html',{'form': form} )    


@login_required
def payment_success(request):
    form = PaymentForm(request.POST)
    template = loader.get_template("payment_success.html")
    if request.method == 'GET':
     return render(request, 'payment_success.html')  
    return render(request, 'payment_success.html')
  
def search (request):
    query = request.GET.get('q')
    if query:
        results_menu = Product.objects.filter(product_name__icontains=query) 
        results_toppick = Toppicks.objects.filter(pick_description__icontains=query)
    else:
        results = None
    template = loader.get_template('search_results.html')
    context = {
        'results_menu': results_menu,
        'results_toppick': results_toppick,
        'results': results
    }
    return HttpResponse(template.render(context, request))
