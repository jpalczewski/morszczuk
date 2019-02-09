from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="Category name", unique=True, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
