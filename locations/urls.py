from django.contrib import admin
from django.urls import path
from locations.views import LocationList, LocationDetail

app_name = "locations"
urlpatterns = [
    path("", LocationList.as_view(), name="location-list"),
    path("<int:pk>/", LocationDetail.as_view(), name="location-detail"),
]
