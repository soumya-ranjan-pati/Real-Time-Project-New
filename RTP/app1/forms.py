from django import forms
from app1.models import *
# *--star means import all the models

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        exclude = ('otp',)

