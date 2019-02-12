from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel


class Item(TimeStampedModel):
    name = models.CharField(verbose_name="Item name", max_length=200)
    count = models.PositiveIntegerField(verbose_name="Count", default=1)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    location = models.ForeignKey("locations.Location", on_delete=models.PROTECT, related_name='items')
    category = models.ForeignKey(
        "categories.Category", on_delete=models.PROTECT, blank=True, null=True, related_name='items'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("items:detail", kwargs={"pk": self.pk})
