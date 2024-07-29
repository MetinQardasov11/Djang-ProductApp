from django.urls import path
from .views import index, products, category_detail, product_detail

app_name = 'product'

urlpatterns = [
    path('', index, name='home'),
    path('products/', products, name='products'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
]