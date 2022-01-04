from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import PictureForm, TestForm
from .models import PictData, TestModel
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PictFormView(LoginRequiredMixin, CreateView):
    form_class = PictureForm
    template_name = "menu/testmodel_form.html"
    success_url = reverse_lazy("menu:top")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "新規データを作成しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "作成に失敗しました")
        return super().form_invalid(form)


class Top(TemplateView):
    model = PictData
    template_name = 'menu/top.html'


class PostLsit(LoginRequiredMixin, ListView):
    model = PictData
    context_object_name = "items"
    template_name = "menu/postlist.html"

    def get_queryset(self):
        return PictData.objects.filter(user=self.request.user)


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






