from django.shortcuts import render
from .models import Mobile

def mobiles_list(request):
    all_mobiles = Mobile.objects.all()
    return render(
        request,
        'mobile/mobile_list.html',
        {'mobiles': all_mobiles}
    )


