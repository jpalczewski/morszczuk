from django.contrib import admin
from .models import Item
from locations.models import Location
from categories.models import Category


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


class CollectionInline(admin.StackedInline):
    model = Location
    extra = 1


class CollectionAdmin(admin.ModelAdmin):
    inlines = [CollectionInline, ItemInline]


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Location, CollectionAdmin)


