from django import forms


class UserDataForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)


class ShippingDataform(forms.Form):
    receiver_first_name = forms.CharField(required=True)
    receiver_last_name = forms.CharField(required=True)
    receiver_address = forms.CharField(required=True)
