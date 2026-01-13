from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from mobiles.views import politika_konf, uslovija_sogl, kontakts, o_nas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mobiles/', include('mobiles.urls', namespace='mobiles')),
    path('', RedirectView.as_view(url='/mobiles/')),
    path('privacy/', politika_konf, name='privacy'),
    path('terms/', uslovija_sogl, name='terms'),
    path('contacts/', kontakts, name='contacts'),
    path('about_us/', o_nas, name='about_us')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
