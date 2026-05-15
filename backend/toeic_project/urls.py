from django.contrib import admin
from django.urls import include, path

from .views import api_root

urlpatterns = [
    path("", api_root, name="root"),
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls")),
]
