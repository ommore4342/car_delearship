import os, json
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


def serve_index(request):
    from djangoapp.models import Dealer
    from djangoapp.populate import seed_dealers

    if Dealer.objects.count() == 0:
        seed_dealers()

    dealers = list(Dealer.objects.order_by('state', 'city').values(
        'id', 'full_name', 'city', 'state', 'zip', 'address', 'phone'
    ))

    user = request.user.username if request.user.is_authenticated else ''
    dealers_json = json.dumps(dealers)

    html_path = os.path.join(settings.BASE_DIR, 'frontend', 'static', 'index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Inject data right before closing body tag
    inject = f'<script>window._PRELOADED_DEALERS={dealers_json};window._CURRENT_USER={json.dumps(user)};</script>'
    html = html.replace('</body>', inject + '</body>')
    return HttpResponse(html, content_type='text/html; charset=utf-8')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('', serve_index, name='home'),
] + static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'frontend', 'static'))
