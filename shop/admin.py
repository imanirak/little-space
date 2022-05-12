from django.contrib import admin
from .models import Shop, Inventory, Item
# Register your models here.

admin.site.register(Shop)
admin.site.register(Inventory)
admin.site.register(Item)