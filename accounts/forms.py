import re
from constance import config

from django import forms

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import (
    RegionalPhoneNumberWidget as PhoneWidget,
)


class FadderEditForm(forms.Form):
    email = forms.EmailField(
        label="Epost",
        required=True,
        help_text="Epost som du kommer få information skickad till.",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )

    name = forms.CharField(
        label="Namn",
        required=False,
        max_length=100,
        help_text="Vad vill du bli kallad?",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    phone_number = PhoneNumberField(
        label="Telefonnummer",
        required=False,
        help_text="Telefonnummer som fadderiet kan kontakta dig på.",
        widget=PhoneWidget(attrs={"class": "form-control"}),
    )

    motto = forms.CharField(
        label="Motto",
        required=False,
        help_text="Motto som visas på topplistan.",
        widget=forms.Textarea(
            attrs={"class": "form-control motto-input", "maxlength": 100, "rows": 3}
        ),
    )

    password = forms.CharField(
        label="Nytt lösenord",
        required=False,
        help_text="Om du vill byta lösenord skriver du in ditt nya här.",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
