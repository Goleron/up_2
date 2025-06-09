from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'shop/home.html'

class AboutView(TemplateView):
    template_name = 'shop/about.html'

class ContactsView(TemplateView):
    template_name = 'shop/contacts.html'

class FindUsView(TemplateView):
    template_name = 'shop/find_us.html'

class ProductsView(TemplateView):
    template_name = 'shop/products.html'

class CategoriesView(TemplateView):
    template_name = 'shop/categories.html'

class AllProductsView(TemplateView):
    template_name = 'shop/all_products.html'

class CartView(TemplateView):
    template_name = 'shop/cart.html'

class ServicesView(TemplateView):
    template_name = 'shop/services.html'

home = HomeView.as_view()
about = AboutView.as_view()
contacts = ContactsView.as_view()
find_us = FindUsView.as_view()
products = ProductsView.as_view()
categories = CategoriesView.as_view()
all_products = AllProductsView.as_view()
cart = CartView.as_view()
services = ServicesView.as_view()