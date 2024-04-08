from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from .models import Product, Splice_display, Toppicks, CartItems_menu,CartItems_toppick

# Create your views here.
def nav (request):
    food_list = Product.objects.all()
    splice_images = Splice_display.objects.all()
    Top_food_picks = Toppicks.objects.all()
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
    #cartitems = []
    #retrieving toppick items from the cart and then using the foreign key relationship to get all the properties of the pick
    toppicks_in_cart = CartItems_toppick.objects.filter(cart_owner = user)
    #for item in toppicks_in_cart:
      #  toppicks_in_cart_photo = item.toppick_cart_product.pick_photo
        #toppicks_in_cart_price = item.toppick_cart_product.pick_price
       # toppicks_in_cart_description = item.toppick_cart_product.pick_description
       

    menu_items_in_cart = CartItems_menu.objects.filter(user_id = user)


    template = loader.get_template("cart_items.html")
    context = {
        "toppicks_in_cart" : toppicks_in_cart,
        "menu_items_in_cart": menu_items_in_cart,
    }
    return HttpResponse(template.render(context, request))



 