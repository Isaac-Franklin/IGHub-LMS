from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("useronboard.urls")),
    path('staff/', include("tutorsapp.urls")),
    path('useronboard/', include("useronboard.urls")),
    path('dashboard/', include("lmsapp.url")),
    path('Dashboard/', include("lmsapp.url")),
    path('user/', include("lmsapp.url")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
