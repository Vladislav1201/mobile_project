from django.urls import path
from mobiles.views import mobiles_list, mobile_detail, politika_konf, uslovija_sogl, kontakts, o_nas, mobile_create, \
    mobile_edit, mobile_delete

app_name = 'mobiles'

urlpatterns = [
    path('', mobiles_list, name='mobiles_list'),
    path('<int:mobile_id>/', mobile_detail, name='mobile_detail'),
    path('privacy/', politika_konf, name='privacy'),
    path('terms/', uslovija_sogl, name='terms'),
    path('contacts/', kontakts, name='contacts'),
    path('about_us', o_nas, name='about_us'),
    path('add/', mobile_create, name="mobile_create"),
    path('<int:mobile_id>/edit/', mobile_edit, name='mobile_edit'),
    path('<int:mobile_id>/delete/', mobile_delete, name='mobile_delete')

]
