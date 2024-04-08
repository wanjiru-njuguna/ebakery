from django.urls import path
from . import views

urlpatterns = [
    path("", views.nav, name="nav") ,
    path("product_details", views.product_details, name="product_details"),
    path("toppick", views.toppick, name="toppick_details"),
    path("add_toppick_tocart", views.toppick_cart, name = "add_toppick_tocart"),
    path("add_menu_tocart", views.CartItem_menu, name = "add_menu_tocart"),
    path("view_cart_items", views.view_cart_items, name = "view_cart_items")

]
