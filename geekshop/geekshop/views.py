from django.shortcuts import render


def index(request):
    title = 'Магазин'
    content = {
        'title': title
    }
    return render(request, 'index.html', context=content)

def contacts(request):
    title = 'Контакты'
    content = {
        'title': title
    }
    return render(request, 'contact.html', context=content)
