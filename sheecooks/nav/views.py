from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nav (request):
    return render(request, 'navbar.html')
