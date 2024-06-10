from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'home.html')

def book_table(request):
    return render(request, 'home.html')

def order(request):
    return render(request, 'home.html')