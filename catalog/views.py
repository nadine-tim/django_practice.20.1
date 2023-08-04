from django.shortcuts import render

from catalog.models import Product


def home(request):
   products_list = Product.objects.all()
   context = {
       'objects_list': products_list,
       'title': 'Главная'
   }
   return render(request,'catalog/home.html', context)

# def index(request):
#     return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name}, {phone}: {message}")
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)