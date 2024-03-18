from django.urls import path
from . import views

urlpatterns = [
    path("", views.nav, name="nav") ,
]
