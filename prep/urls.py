from django.contrib import admin
from django.urls import path
from prep import views

urlpatterns = [
    path("", views.index, name='prep'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("unstructured", views.unstructured, name='unstructured'),
    path("semistructured", views.semistructured, name='semistructured'),
    path("structured", views.structured, name='structured'),
]

