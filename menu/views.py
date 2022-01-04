from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import PictureForm, TestForm
from .models import PictData, TestModel
from django.shortcuts import redirect, render, resolve_url
from django.contrib import messages
from django.urls import reverse, reverse_lazy


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


class TestFormView(CreateView):
    form_class = TestForm
    template_name = "menu/testmodel_form.html"
    success_url = reverse_lazy('menu:testlist')

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' バリデーションに失敗した時 '''
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)


class TestDetailView(DetailView):
    model = TestModel
    template_name = "menu/testmodel_detail.html"
    context_object_name = "item"

class TestListView(ListView):
    model = TestModel
    context_object_name = "items"






