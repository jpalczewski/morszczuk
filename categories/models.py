from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(verbose_name="Category name", unique=True, max_length=50)
    parent = models.ForeignKey('Category', models.CASCADE, verbose_name="Parent category", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories:detail", kwargs={"pk": self.pk})


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
