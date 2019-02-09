from django.contrib import admin
from django.urls import path
from locations.views import LocationList, LocationDetail
#
# app_name = 'categories'
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('collections/', LocationList.as_view(), name='collection-list'),
#     path('collections/<int:pk>/', LocationDetail.as_view(), name='collection-detail')
# ]