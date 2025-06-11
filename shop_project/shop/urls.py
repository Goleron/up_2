from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Статические страницы
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('find_us/', views.find_us, name='find_us'),
    path('products/', views.products, name='products'),
    path('categories/', views.categories, name='categories'),
    path('all-products/', views.all_products, name='all_products'),
    path('cart/', views.cart, name='cart'),
    path('services/', views.services, name='services'),
    # CRUD для Product
    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    # CRUD для Team
    path('teams/list/', views.TeamListView.as_view(), name='team_list'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail'),
    path('teams/create/', views.TeamCreateView.as_view(), name='team_create'),
    path('teams/<int:pk>/update/', views.TeamUpdateView.as_view(), name='team_update'),
    path('teams/<int:pk>/delete/', views.TeamDeleteView.as_view(), name='team_delete'),
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
]