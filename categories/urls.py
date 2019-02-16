from django.contrib import admin
from django.urls import path
from categories.views import CategoryList, CategoryDetail, CategoryCreate, CategoryDelete, CategoryUpdate

app_name = 'categories'
urlpatterns = [
    path('', CategoryList.as_view(), name='list'),
    path('add/', CategoryCreate.as_view(), name='create'),
    path('<int:pk>/', CategoryDetail.as_view(), name='detail'),
    path('<int:pk>/update', CategoryUpdate.as_view(), name='update'),
    path('<int:pk>/delete', CategoryDelete.as_view(), name='delete'),

]
