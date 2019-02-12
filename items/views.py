from items.models import Item

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ItemList(LoginRequiredMixin, ListView):
    model = Item
    extra_context = {"show_actions": True}
    context_object_name = 'items'


class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item
    extra_context = {"show_actions": True}
    context_object_name = 'item'


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ["name", "description", "count", "category", "location"]


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ["name", "description", "count", "category", "location"]


class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy("items:list")



