from django.shortcuts import redirect, render, get_object_or_404
from mobiles.models import Mobile
from django.contrib.auth.decorators import login_required
from korzina.models import Order, OrderItem


@login_required
def add_to_korzina(request, mobile_id):
    mobile = get_object_or_404(Mobile, id=mobile_id)

    korzina = request.session.get('korzina', {})
    korzina[str(mobile_id)] = korzina.get(str(mobile_id), 0) + 1
    request.session['korzina'] = korzina

    return redirect('korzina:view')


@login_required
def korzina_view(request):
    if request.user.is_owner():
        return redirect('mobiles:mobiles_list')

    korzina_session = request.session.get('korzina', {})

    korzina = []
    total_sum = 0

    for mobile_id, quantity in korzina_session.items():
        mobile = get_object_or_404(Mobile, id=mobile_id)

        item_total = mobile.price * quantity
        total_sum += item_total

        korzina.append({
            'mobile': mobile,
            'quantity': quantity,
            'item_total': item_total
        })

    return render(request, 'korzina/korzina.html', {
        'korzina': korzina,
        'total_sum': total_sum
    })


@login_required
def create_order(request):
    korzina = request.session.get('korzina', {})
    if not korzina:
        return redirect('korzina:view')

    order = Order.objects.create(user=request.user)

    for mobile_id, quantity in korzina.items():
        mobile = get_object_or_404(Mobile, id=mobile_id)
        OrderItem.objects.create(
            order=order,
            mobile=mobile,
            quantity=quantity
        )

    request.session['korzina'] = {}
    return redirect('users:profile')


@login_required
def increase_item(request, mobile_id):
    korzina = request.session.get('korzina', {})
    key = str(mobile_id)

    korzina[key] = korzina.get(key, 0) + 1
    request.session['korzina'] = korzina

    return redirect('korzina:view')


@login_required
def decrease_item(request, mobile_id):
    korzina = request.session.get('korzina', {})
    key = str(mobile_id)

    if key in korzina:
        korzina[key] -= 1
        if korzina[key] <= 0:
            del korzina[key]

    request.session['korzina'] = korzina
    return redirect('korzina:view')
