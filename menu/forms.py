from django import forms
from django.db.models import fields
from . import models

class PictureForm(forms.ModelForm):
    class Meta:
        model = models.PictData
        fields = ("user", "picture", "title")


class TestForm(forms.ModelForm):
    class Meta:
        model = models.TestModel
        fields = ("picture", "title", )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'