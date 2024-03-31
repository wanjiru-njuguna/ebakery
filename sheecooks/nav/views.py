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

#def Splice_display (request):
    #splice_images = Splice_display.objects.all().values()
    #template = loader.get_template("nav.html")
    #context = {
       # "splice_images": splice_images,
      #  }
    #return HttpResponse(template.render(context, request))

