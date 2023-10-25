from django.contrib import admin
from django.urls import path, include, re_path
from account.views import Login, Register, activate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("blog.urls")),
    path("", include("django.contrib.auth.urls")),
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path("account/", include("account.urls")),
    path('comment/', include('comment.urls')),
    path("admin/", admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
