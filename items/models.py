from django.db import models


class Item(models.Model):
    item_name = models.CharField(verbose_name="Item name", max_length=200)
    count = models.PositiveIntegerField(verbose_name="Count", default=1)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    location = models.ForeignKey("locations.Location", on_delete=models.PROTECT)
    category = models.ForeignKey(
        "categories.Category", on_delete=models.PROTECT, blank=True, null=True
    )

    def __str__(self):
        return self.item_name
