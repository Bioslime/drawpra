from django import forms
from django.db.models import fields
from . import models


class PictureForm(forms.ModelForm):
    class Meta:
        model = models.PictData
        fields = ("picture", "title")
        labels = {
            "picture" : "登録イラスト ",
            "title" : "イラストタイトル ",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class GoodPointForm(forms.ModelForm):
    class Meta:
        model = models.GoodPoint
        fields = ("text",)
        labels = {
            "text" : "イラストの好きなところ",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MinuteGoodPointForm(forms.ModelForm):
    class Meta:
        model = models.MinuteGoodPoint
        fields = ("text",)
        labels = {
            "text" : "好きなところを詳しく",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class CheckForm(forms.ModelForm):
    class Meta:
        model = models.MinuteGoodPoint
        fields = ("clear_check",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'