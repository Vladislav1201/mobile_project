from django.urls import path
from .views import mobiles_list
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mobiles'

urlpatterns = [
    path('', mobiles_list, name='mobiles_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
