import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


def serve_index(request):
    """Serve index.html with dealers pre-injected as JSON so the page
    never shows 0 dealers even before JS runs."""
    from djangoapp.models import Dealer
    from djangoapp.populate import seed_dealers
    import json

    # Auto-seed on first request
    if Dealer.objects.count() == 0:
        seed_dealers()

    dealers = list(Dealer.objects.order_by('state', 'city').values(
        'id', 'full_name', 'city', 'state', 'zip', 'address', 'phone'
    ))
    dealers_json = json.dumps(dealers)

    # Read the HTML file
    html_path = os.path.join(settings.BASE_DIR, 'frontend', 'static', 'index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Inject pre-loaded dealer data right before </body>
    inject = f"""
<script>
// Pre-loaded dealer data from Django (avoids fetch delay / failures)
window._PRELOADED_DEALERS = {dealers_json};
</script>"""
    html = html.replace('</body>', inject + '\n</body>')

    return HttpResponse(html, content_type='text/html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('', serve_index, name='home'),
] + static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'frontend', 'static'))
