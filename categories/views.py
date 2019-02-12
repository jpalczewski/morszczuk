from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from categories.models import Category


class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    extra_context = {"show_actions": True}
    login_url = '/login/'
    context_object_name = 'categories'


class CategoryDetail(LoginRequiredMixin, DetailView):
    model = Category
    extra_context = {"show_actions": True}
    login_url = '/login/'
    context_object_name = 'category'


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    login_url = '/login/'
    fields = ["name",  "parent"]


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    login_url = '/login/'
    success_url = reverse_lazy('categories:list')


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    login_url = '/login/'
    fields = ["name",  "parent"]

