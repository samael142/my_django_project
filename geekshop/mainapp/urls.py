from django.urls import path
from .views import products, add_productcategory, add_product

app_name = 'mainapp'


urlpatterns = [
    path('', products, name='products'),
    path('<int:pk>/', products, name='category'),
    path('add_category/', add_productcategory, name='add_category'),
    path('add_product/', add_product, name='add_product'),
]
