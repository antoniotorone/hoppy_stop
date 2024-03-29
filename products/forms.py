from django import forms
from .models import Product, Category, Review
from .widgets import CustomClearableFileInput


""" Form that take all the model fields """


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='image', required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'management-form'


""" Form related to the review model with the fields """


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")
