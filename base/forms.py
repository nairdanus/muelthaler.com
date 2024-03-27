from django import forms
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy


class PdfAccessForm(forms.Form):
    captcha = CaptchaField(
        error_messages={"invalid": gettext_lazy("Invalid CAPTCHA")},

    )
