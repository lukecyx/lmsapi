from django.urls import path

from apps.test_utils import dummy_views as views

urlpatterns = [
    path("dummy/", views.DummyView.as_view(), name="dummy-view"),
]
