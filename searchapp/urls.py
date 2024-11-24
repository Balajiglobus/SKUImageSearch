from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_sku, name='search_sku'),
]