from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'descrição', 'preço']  
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descrição': forms.Textarea(attrs={'class': 'form-control'}),
            'preço': forms.NumberInput(attrs={'class': 'form-control'}),
        }
