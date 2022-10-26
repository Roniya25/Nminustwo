from django import forms
from .models import *


class UploadForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ('Name', 'Description', 'Upload_file')

