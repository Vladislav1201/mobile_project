from django.urls import path
from korzina.views import korzina_view, add_to_korzina, create_order, increase_item, decrease_item

app_name = 'korzina'

urlpatterns = [
    path('', korzina_view, name='view'),
    path('add/<int:mobile_id>/', add_to_korzina, name='add'),
    path('create_order/', create_order, name='create_order'),
    path('increase/<int:mobile_id>/', increase_item, name='increase'),
    path('decrease/<int:mobile_id>/', decrease_item, name='decrease'),

]
