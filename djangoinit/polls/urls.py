from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("id", views.view, name="view"),
    path("create", views.create, name="create"),
    path("store", views.store, name="store"),
    path("edit", views.edit, name="edit"),
    path("update", views.update, name="update"),
    path("destroy", views.destroy, name="destroy"),
]
