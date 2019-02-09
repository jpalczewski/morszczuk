from django.views.generic import ListView,DetailView
from .models import Collection, Item


class CollectionList(ListView):
    model = Collection


class CollectionDetail(DetailView):
    model = Collection
    context_object_name = 'collection'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.filter(location=self.get_object())
        context['child_collections'] = Collection.objects.filter(parent_collection=self.get_object())
        return context



