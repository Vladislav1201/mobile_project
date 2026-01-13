from django.shortcuts import render, get_object_or_404, redirect
from mobiles.models import Mobile
from datetime import datetime
from django.contrib.auth.decorators import login_required
from mobiles.forms import MobileForm
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

@login_required
def mobile_create(request):
    if not request.user.is_owner:
        return redirect("mobiles:mobiles_list")

    if request.method == "POST":
        form = MobileForm(request.POST, request.FILES)
        if form.is_valid():
            mobile = form.save(commit=False)
            mobile.owner = request.user
            mobile.save()
            return redirect("mobiles:mobile_detail", mobile_id=mobile.id)
    else:
        form = MobileForm()
    return render(request, "mobile/mobile_create.html", {"form": form})



@login_required
def mobile_edit(request, mobile_id):
    mobile = get_object_or_404(Mobile, id=mobile_id)

    # Только owner может редактировать все телефоны
    if not request.user.is_owner:
        return HttpResponseForbidden("У вас нет прав на редактирование этого телефона")

    if request.method == "POST":
        form = MobileForm(request.POST, request.FILES, instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("mobiles:mobile_detail", mobile_id=mobile.id)
    else:
        form = MobileForm(instance=mobile)

    return render(request, "mobile/mobile_edit.html", {"form": form, "mobile": mobile})


@login_required
def mobile_delete(request, mobile_id):
    mobile = get_object_or_404(Mobile, id=mobile_id)

    if request.method == "POST":
        mobile.delete()
        return redirect("mobiles:mobiles_list")
    return render(
        request,
        "mobile/mobile_confirm_delete.html",
        context={"mobile": mobile}
         )
