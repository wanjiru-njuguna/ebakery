from django.shortcuts import redirect, render
from django.urls import reverse
from functools import wraps
from .models import Cart

def redirect_to_login(function):
    @wraps(function)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))  
        
        return function(request, *args, **kwargs)
    
    return _wrapped_view

def no_null_items_checkout(function):
    @wraps(function)

    def _wrapped_view(request, *args, **kwargs):
        no_of_cart_items =Cart.objects.filter(user_id = request.user).count()

        if no_of_cart_items < 1:
            return render(request,'go_to_cart.html')  
        
        return function(request, *args, **kwargs)
    
    return _wrapped_view

