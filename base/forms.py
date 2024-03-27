from django import forms
from captcha.fields import CaptchaField

class PdfAccessForm(forms.Form):
    captcha = CaptchaField()
