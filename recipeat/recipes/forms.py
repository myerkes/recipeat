from .models import *
from django import forms

### Recipe Forms ###
# class RecipeCreateForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['recipe_url']

class RecipeURLForm(forms.Form):
    recipe_url = forms.URLField(label='Recipe URL', widget=forms.URLInput(attrs={'placeholder': 'Enter recipe URL'}))
