from django.contrib import admin
from django.urls import path
from locations.views import (
    LocationList,
    LocationDetail,
    LocationCreate,
    LocationDelete,
    LocationUpdate,
)

app_name = "locations"
urlpatterns = [
    path("", LocationList.as_view(), name="location-list"),
    path("add", LocationCreate.as_view(), name="location-create"),
    path("<int:pk>/", LocationDetail.as_view(), name="location-detail"),
    path("<int:pk>/update", LocationUpdate.as_view(), name="location-update"),
    path("<int:pk>/delete", LocationDelete.as_view(), name="location-delete"),
]
