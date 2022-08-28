from django.contrib import admin
from django.urls import path
from prep import views

app_name ="prep"

urlpatterns = [
    path("", views.index, name='prep'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("semistructured", views.semistructured, name='semistructured'),
    path("structured", views.structured, name='structured'),
    path("unstructured",views.unstructured),
    path("upload",views.send_files,name="uploads")
]



