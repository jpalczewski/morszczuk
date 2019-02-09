from django.views.generic import ListView, DetailView

from items.models import Item
from locations.models import Location


class LocationList(ListView):
    model = Location


class LocationDetail(DetailView):
    model = Location
    context_object_name = "location"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = Item.objects.filter(location=self.get_object())
        context["child_locations"] = Location.objects.filter(parent=self.get_object())
        return context
