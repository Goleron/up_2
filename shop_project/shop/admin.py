from django.contrib import admin
# from django.contrib.auth.models import User
from .models import Team, Category, Collection, Manufacturer, Product, Inventory, Review, Promotion, Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'pickup_method', 'created_at')
    list_filter = ('pickup_method', 'created_at')
    search_fields = ('user__username', 'id')

admin.site.register(Team)
admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Review)
admin.site.register(Promotion)
admin.site.register(OrderItem)
# admin.site.register(User)
