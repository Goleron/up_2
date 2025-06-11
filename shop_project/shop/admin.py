from django.contrib import admin
from .models import Team, Category, Collection, Manufacturer, Product, Inventory, Review, Promotion

admin.site.register(Team)
admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Review)
admin.site.register(Promotion)