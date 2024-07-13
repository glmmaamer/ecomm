from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Full name'}),required=False)
    shipping_email =forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}),required=False)
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

class PaymentForm(forms.Form):
    card_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'الاسم على البطاقة'}),required=False)
    card_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': ' رقم البطاقة '}),required=False)
    card_exp_date = forms.DateField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'تاريخ إنتهاء البطاقة'}),required=False)
    card_cvv_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'رقم الكود الموجود على بطاقات الاتمان'}),required=False)
    card_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'عنوان البطاقة الاول'}),required=False)
    card_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'عنوان البطاقة الثاني'}),required=False)
    card_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'المدينة'}),required=False)
    card_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'الولاية'}),required=False)
    card_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'كود الفاتورة'}),required=False)
    card_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'البلد'}),required=False)




