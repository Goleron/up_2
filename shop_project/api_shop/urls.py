from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderItemViewSet, TeamViewSet, CategoryViewSet, CollectionViewSet, ManufacturerViewSet, ProductViewSet, InventoryViewSet, ReviewViewSet, PromotionViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'collections', CollectionViewSet)
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'promotions', PromotionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]