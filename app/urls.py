from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("catalogo", views.catalog, name="catalog"),
    path("agenda", views.schedule, name="schedule"),
    path("ubicacion", views.location, name="location")
]
