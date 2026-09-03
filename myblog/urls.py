from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # ബ്ലോഗ് ആപ്പിലെ urls ലിങ്ക് ചെയ്യുന്നു
    path("", include("blog.urls")),
]

# മീഡിയ ഫയലുകൾ ലോക്കലായി ലോഡ് ചെയ്യാൻ ഇത് ചേർക്കുന്നു
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)