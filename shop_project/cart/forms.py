from django import forms

class OrderForm(forms.Form):
    pickup_method = forms.ChoiceField(choices=[
        ('store', 'Самовывоз из магазина'),
        ('courier', 'Курьер'),
        ('post', 'Почта'),
    ], widget=forms.RadioSelect)

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=100, initial=1, label="Количество")
    reload = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
