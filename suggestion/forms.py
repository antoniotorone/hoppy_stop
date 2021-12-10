from django import forms
from .models import ProductSuggestion

""" Form that take all fields and use for submit the user suggestion """


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = ProductSuggestion
        fields = '__all__'
