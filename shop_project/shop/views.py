from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Team, Category, Collection, Promotion
from .forms import ProductForm, TeamForm, CategoryForm, CollectionForm, PromotionForm

# Статические страницы
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

# CRUD для Product
class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('shop:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('shop:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    success_url = reverse_lazy('shop:product_list')

# CRUD для Team
class TeamListView(ListView):
    model = Team
    template_name = 'shop/team_list.html'
    context_object_name = 'teams'

class TeamDetailView(DetailView):
    model = Team
    template_name = 'shop/team_detail.html'
    context_object_name = 'team'

class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'shop/team_form.html'
    success_url = reverse_lazy('shop:team_list')

class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'shop/team_form.html'
    success_url = reverse_lazy('shop:team_list')

class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'shop/team_confirm_delete.html'
    success_url = reverse_lazy('shop:team_list')

# CRUD для Category
class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'shop/category_form.html'
    success_url = reverse_lazy('shop:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'shop/category_form.html'
    success_url = reverse_lazy('shop:category_list')

class CategoryDeleteView(UpdateView):
    model = Category
    template_name = 'shop/category_confirm_delete.html'
    success_url = reverse_lazy('shop:category_list')


class CollectionListView(ListView):
    model = Collection
    template_name = 'shop/collection_list.html'
    context_object_name = 'collections'

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'shop/collection_detail.html'
    context_object_name = 'collection'

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'shop/collection_form.html'
    success_url = reverse_lazy('shop:collection_list')

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'shop/collection_form.html'
    success_url = reverse_lazy('shop:collection_list')

class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'shop/collection_confirm_delete.html'
    success_url = reverse_lazy('shop:collection_list')


class PromotionListView(ListView):
    model = Promotion
    template_name = 'shop/promotion_list.html'
    context_object_name = 'promotions'

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'shop/promotion_detail.html'
    context_object_name = 'promotion'

class PromotionCreateView(CreateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'shop/promotion_form.html'
    success_url = reverse_lazy('shop:promotion_list')

class PromotionUpdateView(UpdateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'shop/promotion_form.html'
    success_url = reverse_lazy('shop:promotion_list')

class PromotionDeleteView(DeleteView):
    model = Promotion
    template_name = 'shop/promotion_confirm_delete.html'
    success_url = reverse_lazy('shop:promotion_list')