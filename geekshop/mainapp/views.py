import json

from django.shortcuts import render
from .models import Product, ProductCategory

# Create your views here.
def products(request, id=None):
    print(id)
    title = 'Продукты'
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all()
    content = {
        'links_menu': links_menu,
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/products.html', context=content)

# Заполняем базу из файлов
def add_productcategory(request):
    # with open('mainapp/ProductCategory.json') as f:
    #     templates = json.load(f)
    # for item in templates['ProductCategory']:
    #     new_category = ProductCategory(name=item)
    #     new_category.save()
    return render(request, 'mainapp/import.html')

def add_product(request):
    # with open('mainapp/products.json') as f:
    #     templates = json.load(f)
    #     for item in templates:
    #         new_product = Product(name=item['name'],
    #                               category_id=item['category'],
    #                               image=item['image'],
    #                               price=item['price'],
    #                               quantity=item['quantity'])
    #         new_product.save()
    return render(request, 'mainapp/import.html')

