from django.contrib import admin
from .models import Product, Order,Splice_display,Toppicks,CartItems_toppick,CartItems_menu

#Register your models here.
nav_models = [Product,Order,Splice_display,Toppicks, CartItems_toppick,CartItems_menu]
admin.site.register(nav_models)