from django.contrib import admin
from .models import User, Product, Order

# Register your models here.
nav_models = [User, Product,Order ]
admin.site.register(nav_models)