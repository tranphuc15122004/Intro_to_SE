from django.shortcuts import render
from app.models import Category , Product
# Create your views here.


def Mater(request):
    return render(request ,'master.html')

def Index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'category' : category,
        'product' : product,
    }
    return render(request , 'index.html' , context)
