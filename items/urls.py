from django.urls import path
from items.views import ItemList, ItemCreate, ItemDetail, ItemUpdate, ItemDelete
app_name = "items"
urlpatterns = [
    path("", ItemList.as_view(), name="list"),
    path("add", ItemCreate.as_view(), name="create"),
    path("<int:pk>/", ItemDetail.as_view(), name="detail"),
    path("<int:pk>/update", ItemUpdate.as_view(), name="update"),
    path("<int:pk>/delete", ItemDetail.as_view(), name="delete"),
]
