from django import forms
from .models import Basic_data

class PostForm(forms.ModelForm):

    class Meta:
        model = Basic_data
        fields = ("place_name", "travel_expenses", "hotel_expenses",
        "religion", "info")
