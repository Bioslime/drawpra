from django.views.generic import TemplateView, FormView
from .forms import PictureForm
from django.shortcuts import render
from django.http import HttpResponse



class FormView(TemplateView):
    def __init__(self):
        self.params = {
            "Messeage": "データを入力してください",
            "form": PictureForm(),
        }
