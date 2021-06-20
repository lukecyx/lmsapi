from django.urls import path

from apps.users import views

urlpatterns = [
    path("create/", views.CreateUser.as_view(), name="create-user"),
    # path("delete/", views.DeleteUser.as_view(), name="delete-user"),
]
