from django.contrib import admin
from .models import Category, Item, Collection
# Register your models here.

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Collection)
