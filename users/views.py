from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login
from django.shortcuts import redirect
from users.forms import SignUpForm, UserProfileForm
from django.contrib.auth.decorators import login_required

def signup_view(request: HttpRequest):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("mobiles:mobiles_list")
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", context={
        'form': form
    })

@login_required
def prifile_view(request):
    user = request.user

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)


    return render(request, "users/profile.html", {"form": form})



