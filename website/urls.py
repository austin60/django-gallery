from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name='index'),
    path("cont", views.contact, name='cont'),
    path("prod", views.products, name='prod'),
    path("ab", views.about, name="ab"),
]