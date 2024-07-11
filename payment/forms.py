from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    Shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Full name'}),required=True)
    Shipping_email =forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}),required=True)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address 1'}),required=True)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address 2'}),required=True)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'City'}),required=True)
    shipping_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'State'}),required=True)
    shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Zipcode'}),required=True)
    shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Country'}),required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name','shipping_email','shipping_address1','shipping_address2','shipping_city','shipping_state','shipping_zipcode','shipping_country']

        exclude = ['user',]