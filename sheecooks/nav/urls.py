from django.urls import path
from . import views, remove_from_cart, decorators

urlpatterns = [
    path("", views.nav, name="nav") ,
    path("product_details", views.product_details, name="product_details"),
    path("add_items_tocart", views.add_items_tocart, name = "add_items_tocart"),
    path("view_cart_items", views.view_cart_items, name = "view_cart_items"),
    path("client_checkout", views.client_checkout, name = "client_checkout"),
    path("payment_success", views.payment_success, name="payment_success"),
    path('search/', views.search, name='search'),
    path("remove_from_cart", remove_from_cart.remove_items_from_cart, name="remove_from_cart"),
    path("reduce_cart_item_by_one", remove_from_cart.reduce_cart_item_by_one, name="reduce_cart_item_by_one"),
    path("add_one_item_tocart",remove_from_cart.add_one_item_tocart, name= "add_one_item_tocart"),
    #path("go_to_cart", decorators.no_null_items_checkout, name='go_to_cart' )
]


