from django import forms
from mobiles.models import Mobile


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        exclude = ("owner",)
