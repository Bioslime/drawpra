from django.views.generic import TemplateView
from .forms import PictureForm
from .models import PictData
from django.shortcuts import render
from django.http import HttpResponse


class PictFormView(TemplateView):
    def __init__(self):
        self.params = {
            "title":"画像投稿",
            "Message": "データを入力してください",
            "form": PictureForm(),
        }

    def get(self, request):
        return render(request, "menu/form.html", context=self.params)

    def post(self, request):
        if request.method == "POST":
            self.params["form"] = PictureForm(request.POST)

            if self.params["form"].is_valid():
                self.params["form"].save()
                self.params["Message"] = "送信されました"

        return render(request, "menu/form.html", context=self.params)


class TestFormView(TemplateView):
    pass