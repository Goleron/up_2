from django import forms
from .models import Product, Team, Category, Collection, Promotion

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'size', 'photo', 'is_available', 'category', 'team', 'manufacturer', 'collection']
        widgets = {
            'collection': forms.CheckboxSelectMultiple(),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description', 'logo']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'description', 'year']

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['name', 'discount_percent', 'start_date', 'end_date', 'products']
        widgets = {
            'products': forms.CheckboxSelectMultiple(),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }