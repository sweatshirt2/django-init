from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("store", views.store, name="store"),
    path("<int:question_id>", views.show, name="show"),
    path("<int:question_id>/edit", views.edit, name="edit"),
    path("<int:question_id>/update", views.update, name="update"),
    path("<int:question_id>/results", views.result, name="result"),
    path("<int:question_id>/vote", views.vote, name="vote"),
    path("<int:question_id>/destroy", views.destroy, name="destroy"),
]
