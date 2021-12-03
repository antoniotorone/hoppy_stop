from django import forms
from .models import ProductSuggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = ProductSuggestion
        fields = ("name", "comment", "style")
