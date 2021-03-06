from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from items.models import Item
from locations.models import Location


class LocationCreate(LoginRequiredMixin, CreateView):
    model = Location
    fields = ["name", "description", "parent"]
    login_url = '/login/'


class LocationUpdate(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ["name", "description", "parent"]
    login_url = '/login/'


class LocationDelete(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = reverse_lazy("locations:location-list")
    login_url = '/login/'


class LocationList(LoginRequiredMixin, ListView):
    model = Location
    extra_context = {"show_actions": True}
    login_url = '/login/'


class LocationDetail(LoginRequiredMixin, DetailView):
    model = Location
    context_object_name = "location"
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = Item.objects.filter(location=self.get_object())
        context["child_locations"] = Location.objects.filter(parent=self.get_object())
        context["show_actions"] = True
        return context
