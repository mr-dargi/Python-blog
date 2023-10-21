from django.contrib import admin
from django.urls import path, include
from account.views import Login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("blog.urls")),
    path("", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("login/", Login.as_view(), name="login"),
    path("account/", include("account.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
