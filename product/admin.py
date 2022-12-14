from django.contrib import admin

from .models import ItemType, ItemSizes, Image, Item, Tag, Description, ItemFeature, Inventory, InventoryLog, Customer, Order


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemSizes)
class ItemSizesAdmin(admin.ModelAdmin):
    pass


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemFeature)
class ItemFeatureAdmin(admin.ModelAdmin):
    pass


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(InventoryLog)
class InventoryLogAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
