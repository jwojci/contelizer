from django import forms
from django.core.validators import RegexValidator


class PESELForm(forms.Form):
    # added max_length even tho it is not necessary just so in the form field the user can't enter more than 11 characters
    pesel = forms.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex="^\d{11}$",
                message="PESEL length must be 11 and contain only digits",
            )
        ],
    )
