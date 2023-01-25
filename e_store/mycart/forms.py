from django import forms

class CartItemForm(forms.Form):
    product = forms.CharField()
    quantity = forms.IntegerField()
    cart = forms.CharField()


