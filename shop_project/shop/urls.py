from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('find-us/', views.find_us, name='find_us'),
    path('products/', views.products, name='products'),
    path('categories/', views.categories, name='categories'),
    path('all-products/', views.all_products, name='all_products'),
    path('cart/', views.cart, name='cart'),
    path('services/', views.services, name='services'),
]