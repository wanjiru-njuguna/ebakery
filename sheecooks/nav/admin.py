from django.contrib import admin
from .models import User, Product, Order,Splice_display,Toppicks

#Register your models here.
nav_models = [User, Product,Order,Splice_display,Toppicks ]
admin.site.register(nav_models)