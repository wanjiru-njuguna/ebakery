from django import forms

class PaymentForm(forms.Form):
    delivery_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    card_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    expiry_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cardholder_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cvc_number = forms.CharField(max_length=3)

    