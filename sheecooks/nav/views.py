from django.http import HttpResponse
from django.template import loader
from .models import Product, Splice_display, Toppicks

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



