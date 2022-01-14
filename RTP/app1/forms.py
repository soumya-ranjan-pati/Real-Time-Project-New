from django import forms
from app1.models import *
# *--star means import all the models

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    #otp validation
    def clean_otp(self):
        otp = self.cleaned_data['otp']
        return 5475
    class Meta:
        model = RegistrationModel
        exclude = ('status',)
        #exclude means not include

