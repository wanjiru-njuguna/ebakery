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
from .decorators import redirect_to_login, no_null_items_checkout



# Create your views here.
def nav (request):
    food_list = Product.objects.all()
    splice_images = Splice_display.objects.all()
    if request.user.is_authenticated:
        user = request.user
        no_of_items_in_cart = Cart.objects.filter(user_id = user).count()
    else:
        no_of_items_in_cart = 0

    template = loader.get_template("nav.html")
    context = {
        "food_list": food_list,
        "splice_images": splice_images,
        "no_of_items_in_cart": no_of_items_in_cart
        }
    return HttpResponse(template.render(context, request))


def product_details(request):
    try:
        product_id = request.GET['product_serial_no'] #gets the id of the item from the users request.

        item = Product.objects.get(product_serial_no =product_id)
        context = {
        "prod_sn": product_id,
        "food": item, }
        template = loader.get_template("product_details.html")
    except Exception as e:
        #print(f"#EXCEPTION: {e}\n")
        item = None
        context = {
            "error":e
        }
        template = loader.get_template("exception.html")

    
    return HttpResponse(template.render(context, request))


#function to add items to cart when the add to cart button is clicked on the toppick items. The user needs to be logged in to add items to cart, hence the @loginrequired decorater.


#this is the function for adding the items to cart.
#@login_required
@redirect_to_login
def add_items_tocart(request):
    if request.method == 'POST':
        menu_id = request.POST.get('food_id')
        menu_name = request.POST.get('food_name')

    try:
        menu_item = Product.objects.get(product_serial_no = menu_id)

    except Product.DoesNotExist:
        return redirect('add_items_tocart')

    menucart_item = Cart(user_id = request.user, cart_product_id = menu_item)
    menucart_item.save()
    #messages.success(request, 'Item added to cart.')
    return HttpResponseRedirect ("/")



#this is the shopping cart items views associated with a specific logged in user.

@redirect_to_login
def view_cart_items (request):
    user = request.user
    cart_menu = Cart.objects.filter(user_id = user).all()

    
    menu_items_in_cart = Cart.objects.filter(user_id=user).values('cart_product_id__product_name', 'cart_product_id__product_selling_price','cart_product_id__product_serial_no','cart_product_id__photo' ).annotate(number_items=Count('cart_product_id'))

    total_menu_incart = cart_menu.count()


    template = loader.get_template("cart_items.html")
    context = {
        "menu_items_in_cart": menu_items_in_cart,
        "total_menu_incart": total_menu_incart,
    }
    return HttpResponse(template.render(context, request))
@redirect_to_login
def count_cart_items (user):
    no_of_items_in_cart = Cart.objects.filter(user_id = user).count()
    return no_of_items_in_cart




@redirect_to_login
@no_null_items_checkout
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
        #checking that the cart is not empty
        # elif no_of_cart_items <= 0:
        #     return HttpResponseRedirect ("/payment_failed")

        else:
            form = PaymentForm()
        
    return render(request, 'checkout.html',{'form': form} )    


@redirect_to_login
def payment_success(request):
    form = PaymentForm(request.POST)
    template = loader.get_template("payment_success.html")
    if request.method == 'GET':
     return render(request, 'payment_success.html')  
    return render(request, 'payment_success.html')
  
def search (request):
    if request.method == 'GET':
        query = request.GET.get("q")
        if query:
            results_menu = Product.objects.filter(product_name__icontains=query) 
        
        template = loader.get_template('search_results.html')
        context = {
            'results_menu': results_menu,
            'query': query
        }
        return render(request, 'search_results.html', context,)
    else:
        return render(request, 'search_results.html')

