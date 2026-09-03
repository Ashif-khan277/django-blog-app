from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    # ബ്ലോഗ് ആപ്പിലെ urls ലിങ്ക് ചെയ്യുന്നു
    path("", include("blog.urls")),
    # പ്രൊഡക്ഷനിലും മീഡിയ ഫയലുകൾ കാണിക്കാൻ
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]