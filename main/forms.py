from django import forms
from .models import VideoUrl


class CreateVideoForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Song name'}))
    url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Video URL'}))

    class Meta:
        model = VideoUrl
        fields = ['name', 'url']
