from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("apps.users.urls")),
]

# Used for testing base api calls.
if settings.IS_LOCAL or settings.IS_TEST:
    urlpatterns += [
        path("", include("apps.test_utils.urls")),
    ]
