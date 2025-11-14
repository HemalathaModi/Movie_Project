from django import forms
from .models import Movieinfo

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movieinfo
        fields = ['title', 'description', 'year', 'image']