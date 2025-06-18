from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('find_us/', views.FindUsView.as_view(), name='find_us'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('all-products/', views.AllProductsView.as_view(), name='all_products'),
    path('services/', views.ServicesView.as_view(), name='services'),
    # CRUD для Product
    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    # CRUD для Team
    path('teams/list/', views.TeamListView.as_view(), name='team_list'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail'),
    # CRUD для Category
    path('categories/list/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    # CRUD для Collection
    path('collections/list/', views.CollectionListView.as_view(), name='collection_list'),
    path('collections/<int:pk>/', views.CollectionDetailView.as_view(), name='collection_detail'),
    path('collections/create/', views.CollectionCreateView.as_view(), name='collection_create'),
    path('collections/<int:pk>/update/', views.CollectionUpdateView.as_view(), name='collection_update'),
    path('collections/<int:pk>/delete/', views.CollectionDeleteView.as_view(), name='collection_delete'),
    # CRUD для Promotion
    path('promotions/list/', views.PromotionListView.as_view(), name='promotion_list'),
    path('promotions/<int:pk>/', views.PromotionDetailView.as_view(), name='promotion_detail'),
    path('promotions/create/', views.PromotionCreateView.as_view(), name='promotion_create'),
    path('promotions/<int:pk>/update/', views.PromotionUpdateView.as_view(), name='promotion_update'),
    path('promotions/<int:pk>/delete/', views.PromotionDeleteView.as_view(), name='promotion_delete'),
    # Авторизация и регистрация
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]