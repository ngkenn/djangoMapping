from django.contrib import admin
from django.urls import path, include
from .views import listMappingsView


urlpatterns = [
    path('mappings/', listMappingsView.as_view(), name = 'mappings'),
]