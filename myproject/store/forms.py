from django import forms
from .models import Goods

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['title', 'description', 'category', 'image', 'price', 'date']