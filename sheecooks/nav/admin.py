from django.contrib import admin
from .models import Product, Order,Splice_display,Toppicks,CartItems

#Register your models here.
nav_models = [Product,Order,Splice_display,Toppicks, CartItems]
admin.site.register(nav_models)