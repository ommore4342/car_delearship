from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os

def serve_index(request):
    """Serve the main index.html from frontend/static."""
    from django.http import FileResponse
    index_path = os.path.join(settings.BASE_DIR, 'frontend', 'static', 'index.html')
    return FileResponse(open(index_path, 'rb'), content_type='text/html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('', serve_index, name='home'),
] + static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'frontend', 'static'))
