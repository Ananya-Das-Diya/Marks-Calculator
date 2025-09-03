from django.contrib import admin
from django.urls import path, include
from accounts.views import register_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/register/", register_view, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),  # login/logout
]
