from django import forms
from django.forms import CharField, EmailField, PasswordInput


class RegForm(forms.Form):
    name = CharField(
        label="Your Name",
        required=True,
        strip=True)
    pword = PasswordInput()
    emaill = EmailField(label="Your Email",
                        required=True, )
