from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User, Role

class SignUpForm(UserCreationForm):
    role = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        empty_label=None,
        widget=forms.RadioSelect,
        label="Роль"

    )
    username = forms.CharField(
        label="Имя пользовавателя",
        help_text=None
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        help_text=None
    )

    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
        help_text=None
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'role', 'password1', 'password2')
        help_texts = {
            'username': None,

        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email']

        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Телефон',
            'email': 'Email',


        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }