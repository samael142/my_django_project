import json

from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import Basket

# Create your views here.
def products(request, pk=None):
    title = 'Продукты'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all()
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        content = {
            'title': title,
            'links_menu': links_menu,
            'products': products,
            'category': category,
            'basket': basket,
        }
        return render(request=request, template_name='mainapp/products.html', context=content)
    content = {
        'links_menu': links_menu,
        'title': title,
        'products': products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context=content)

# Заполняем базу из файлов
def add_productcategory(request):
    with open('mainapp/ProductCategory.json') as f:
        templates = json.load(f)
    for item in templates['ProductCategory']:
        new_category = ProductCategory(name=item)
        new_category.save()
    return render(request, 'mainapp/import.html')

def add_product(request):
    with open('mainapp/products.json') as f:
        templates = json.load(f)
        for item in templates:
            new_product = Product(name=item['name'],
                                  category_id=item['category'],
                                  image=item['image'],
                                  price=item['price'],
                                  quantity=item['quantity'])
            new_product.save()
    return render(request, 'mainapp/import.html')

