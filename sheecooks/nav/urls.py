from django.urls import path
from . import views

urlpatterns = [
    path("", views.nav, name="nav") ,
    path("product_details", views.product_details, name="product_details"),
    path("toppick", views.toppick, name="toppick_details")

]
