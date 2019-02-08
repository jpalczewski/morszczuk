from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Category name", unique=True, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Collection(models.Model):
    collection_name = models.CharField(verbose_name='Collection name', max_length=200)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    parent_collection = models.ForeignKey('Collection', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.collection_name


class Item(models.Model):
    item_name = models.CharField(verbose_name="Item name", max_length=200)
    count = models.PositiveIntegerField(verbose_name="Count", default=1)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    location = models.ForeignKey('Collection', on_delete=models.PROTECT)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.item_name
