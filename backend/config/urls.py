from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/houses/", include("houses.api.v1.urls")),
    # path("api/v1/users/", include("users.api.v1.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
