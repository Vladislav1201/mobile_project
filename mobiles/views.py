from django.shortcuts import render, get_object_or_404
from .models import Mobile
from datetime import datetime

def mobiles_list(request):
    mobiles = Mobile.objects.all()
    return render(request, 'mobile/mobile_list.html', {
        'mobiles': mobiles,
        'current_year': datetime.now().year,
    })


def mobile_detail(request, mobile_id):
    mobile = get_object_or_404(Mobile, pk=mobile_id)
    return render(request, 'mobile/mobile_detail.html', {
        'mobile': mobile,
        'current_year': datetime.now().year,
    })

def politika_konf(request):
    return render(request, 'mobile/politika_konf.html')

def uslovija_sogl(request):
    return render(request, 'mobile/uslovija_sogl.html')

def kontakts(request):
    return render(request, 'mobile/kontakts.html')

def o_nas(request):
    return render(request, 'mobile/o_nas.html')


