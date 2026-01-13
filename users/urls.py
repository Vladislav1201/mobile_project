from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import signup_view, prifile_view

app_name = "users"

urlpatterns = [
    path("signup/", signup_view, name="signup"),

    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login"
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="/"),
        name="logout"
    ),

    path('profile/', prifile_view, name='profile'),
]
