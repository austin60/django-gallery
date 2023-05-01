from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def products(request):
    data=Post.objects.all()
    return render(request, "products.html",{"data":data})

