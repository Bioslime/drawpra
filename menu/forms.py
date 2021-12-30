from django import forms
from . import models

class PictureForm(forms):
    class Meta:
        model = models.PictData
        fields = ("picture", "url", "title")