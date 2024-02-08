from django import forms
from django_gems.jewelry.models import Category


class IndexForm(forms.Form):
    categories = Category.TitleChoices.choices

    category = forms.ChoiceField(
        categories=categories,
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )
