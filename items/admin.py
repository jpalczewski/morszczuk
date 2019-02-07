from django.contrib import admin
from .models import Category, Item, Collection


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


class CollectionInline(admin.StackedInline):
    model = Collection
    extra = 1


class CollectionAdmin(admin.ModelAdmin):
    inlines = [CollectionInline, ItemInline]


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Collection, CollectionAdmin)


