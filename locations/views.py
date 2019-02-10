from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from items.models import Item
from locations.models import Location


class LocationCreate(CreateView):
    model = Location
    fields = ["name", "description", "parent"]


class LocationUpdate(UpdateView):
    model = Location
    fields = ["name", "description", "parent"]


class LocationDelete(DeleteView):
    model = Location
    success_url = reverse_lazy("locations:location-list")


class LocationList(ListView):
    model = Location
    extra_context = {"show_actions": True}


class LocationDetail(DetailView):
    model = Location
    context_object_name = "location"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = Item.objects.filter(location=self.get_object())
        context["child_locations"] = Location.objects.filter(parent=self.get_object())
        context["show_actions"] = True
        return context
