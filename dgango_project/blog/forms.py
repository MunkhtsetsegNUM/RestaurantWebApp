from django import forms
from .models import Review

#form тодорхойлж байна.
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rate', 'author']