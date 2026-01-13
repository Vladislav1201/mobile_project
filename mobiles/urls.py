from django.urls import path
from mobiles.views import mobiles_list, mobile_detail, politika_konf, uslovija_sogl, kontakts, o_nas

app_name = 'mobiles'  # важно, чтобы namespace работал в project urls

urlpatterns = [
    path('', mobiles_list, name='mobiles_list'),
    path('<int:mobile_id>/', mobile_detail, name='mobile_detail'),
    path('privacy/', politika_konf, name='privacy'),
    path('terms/', uslovija_sogl, name='terms'),
    path('contacts/', kontakts, name='contacts'),
    path('about_us', o_nas, name='about_us')

]
