from django.db import models
from django.urls import reverse


class Location(models.Model):
    name = models.CharField(verbose_name="Location name", max_length=200)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    parent = models.ForeignKey(
        "Location", on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("locations:location-detail", kwargs={"pk": self.pk})
