from django import forms
from .models import Image

class ImageUploadForm(forms.Form):
    file = forms.FileField(label='Select a file')