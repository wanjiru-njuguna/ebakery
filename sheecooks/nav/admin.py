from django.contrib import admin
from .models import Product,Order,Splice_display,Cart, checkout_information
#Register your models here.
nav_models = [Product,Order,Splice_display,Cart, checkout_information]
admin.site.register(nav_models)