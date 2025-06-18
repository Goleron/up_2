from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Product, Team, Category, Collection, Promotion, Order, OrderItem
from .forms import ProductForm, TeamForm, CategoryForm, CollectionForm, PromotionForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Статические страницы
class HomeView(TemplateView):
    template_name = 'shop/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class AboutView(TemplateView):
    template_name = 'shop/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class ContactsView(TemplateView):
    template_name = 'shop/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class FindUsView(TemplateView):
    template_name = 'shop/find_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class ProductsView(TemplateView):
    template_name = 'shop/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class CategoriesView(TemplateView):
    template_name = 'shop/categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class AllProductsView(TemplateView):
    template_name = 'shop/all_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class ServicesView(TemplateView):
    template_name = 'shop/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

# CRUD для Product
class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.can_add_product'
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('shop:product_list')

class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.can_change_product'
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('shop:product_list')

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.can_delete_product'
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    success_url = reverse_lazy('shop:product_list')

# CRUD для Team
class TeamListView(ListView):
    model = Team
    template_name = 'shop/team_list.html'
    context_object_name = 'teams'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class TeamDetailView(DetailView):
    model = Team
    template_name = 'shop/team_detail.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()
        context['cart'] = Cart(self.request)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

# CRUD для Category
class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        context['categories_with_products'] = [
            {'category': category, 'products': category.products.all()}
            for category in context['categories']
        ]
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        context['category_products'] = self.object.products.all()
        product_ids = self.object.products.values_list('id', flat=True)
        context['collections'] = Collection.objects.filter(products__id__in=product_ids).distinct()
        context['collection_products'] = {
            collection.id: collection.products.all()
            for collection in context['collections']
        }
        return context

class CategoryCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.can_add_category'
    model = Category
    form_class = CategoryForm
    template_name = 'shop/category_form.html'
    success_url = reverse_lazy('shop:category_list')

class CategoryUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.can_change_category'
    model = Category
    form_class = CategoryForm
    template_name = 'shop/category_form.html'
    success_url = reverse_lazy('shop:category_list')

class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.can_delete_category'
    model = Category
    template_name = 'shop/category_confirm_delete.html'
    success_url = reverse_lazy('shop:category_list')

# CRUD для Collection
class CollectionListView(ListView):
    model = Collection
    template_name = 'shop/collection_list.html'
    context_object_name = 'collections'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'shop/collection_detail.html'
    context_object_name = 'collection'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class CollectionCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.can_add_collection'
    model = Collection
    form_class = CollectionForm
    template_name = 'shop/collection_form.html'
    success_url = reverse_lazy('shop:collection_list')

class CollectionUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.can_change_collection'
    model = Collection
    form_class = CollectionForm
    template_name = 'shop/collection_form.html'
    success_url = reverse_lazy('shop:collection_list')

class CollectionDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.can_delete_collection'
    model = Collection
    template_name = 'shop/collection_confirm_delete.html'
    success_url = reverse_lazy('shop:collection_list')

class PromotionListView(ListView):
    model = Promotion
    template_name = 'shop/promotion_list.html'
    context_object_name = 'promotions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'shop/promotion_detail.html'
    context_object_name = 'promotion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff if self.request.user.is_authenticated else False
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class PromotionCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.can_add_promotion'
    model = Promotion
    form_class = PromotionForm
    template_name = 'shop/promotion_form.html'
    success_url = reverse_lazy('shop:promotion_list')

class PromotionUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.can_change_promotion'
    model = Promotion
    form_class = PromotionForm
    template_name = 'shop/promotion_form.html'
    success_url = reverse_lazy('shop:promotion_list')

class PromotionDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.can_delete_promotion'
    model = Promotion
    template_name = 'shop/promotion_confirm_delete.html'
    success_url = reverse_lazy('shop:promotion_list')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в аккаунт!')
            next_url = request.GET.get('next', reverse_lazy('shop:home'))
            return redirect(next_url)
        else:
            messages.error(request, 'Неверные данные авторизации!')
    else:
        form = LoginForm()
    return render(request, 'shop/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация успешна! Пожалуйста, войдите.')
            return redirect('shop:login')
        else:
            messages.error(request, 'Ошибка регистрации. Проверьте данные.')
    else:
        form = RegisterForm()
    return render(request, 'shop/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из аккаунта.')
    return redirect('shop:home')