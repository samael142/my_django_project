from django.shortcuts import render

# Create your views here.
def products(request):
    title = 'Продукты'
    links_menu = [
        {'href': '#', 'name': 'все'},
        {'href': '#', 'name': 'дом'},
        {'href': '#', 'name': 'офис'},
        {'href': '#', 'name': 'модерн'},
        {'href': '#', 'name': 'классика'},
    ]
    content = {
        'links_menu': links_menu,
        'title': title
    }
    return render(request, 'mainapp/products.html', context=content)
