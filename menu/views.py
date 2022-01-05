from django.db.models.base import Model
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import PictureForm, GoodPointForm, MinuteGoodPointForm
from .models import GoodPoint, PictData, MinuteGoodPoint
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import ModelFormMixin

class PictFormView(LoginRequiredMixin, CreateView):
    form_class = PictureForm
    template_name = "menu/pictform.html"
    success_url = reverse_lazy("menu:postlist")

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class PostDetail(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = PictData
    template_name = "menu/postdetail.html"
    context_object_name = "item"

    def test_func(self):
        post_object = self.get_object()
        return self.request.user.id == post_object.user.id

    def handle_no_permission(self):
        return redirect("menu:postlist")


class GoodPointFormview(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy("menu:top")
    form_class = GoodPointForm
    template_name = "menu/good_point_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "新規データを作成しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "作成に失敗しました")
        return super().form_invalid(form)


class PictDetailGoodPost(UserPassesTestMixin, LoginRequiredMixin, DetailView, ModelFormMixin):
    model = PictData
    template_name = "menu/pictdetail_goodpost.html"
    fields = ()
    context_object_name = "item"

    def get_success_url(self):
        return reverse('menu:postdetail', kwargs={"pk":self.kwargs['pk']})

    def test_func(self):
        post_object = self.get_object()
        return self.request.user.id == post_object.user.id

    def handle_no_permission(self):
        return redirect("menu:postlist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "goodpoint_form":GoodPointForm,
            "goodpoint_model":GoodPoint.objects.filter(pict=self.object),
        })
        return context

    def post(self, request, *args, **kwargs):
        print(self.kwargs)
        if 'button_change_goodpoint' in request.POST:
            form_obj = GoodPointForm(**self.get_form_kwargs())
            if form_obj.is_valid():
                form_obj_query = form_obj.save(commit=False)
                form_obj_query.pict = self.model.objects.get(id=self.kwargs["pk"])
                form_obj_query.save()
                return self.form_valid(form_obj)

            else:
                self.object = self.get_object()
                return self.form_invalid(form_obj)


class GoodPointDetail(UserPassesTestMixin, LoginRequiredMixin, DetailView, ModelFormMixin ):
    model = GoodPoint
    template_name = "menu/goodpointdetail.html"
    fields = ()
    context_object_name = "item"

    def get_success_url(self):
        return reverse('menu:goodpointdetail', kwargs={"pk":self.kwargs['pk']})

    def test_func(self):
        post_object = self.get_object()
        return self.request.user.id == post_object.pict.user.id

    def handle_no_permission(self):
        return redirect("menu:postlist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "minuteGP_form":GoodPointForm,
            "minuteGP_model":MinuteGoodPoint.objects.filter(gopo=self.object),
        })
        return context

    def post(self, request, *args, **kwargs):
        print(self.kwargs)
        if 'button_change_minuteGP' in request.POST:
            form_obj = MinuteGoodPointForm(**self.get_form_kwargs())
            if form_obj.is_valid():
                form_obj_query = form_obj.save(commit=False)
                form_obj_query.gopo = self.model.objects.get(id=self.kwargs["pk"])
                form_obj_query.save()
                return self.form_valid(form_obj)

            else:
                self.object = self.get_object()
                return self.form_invalid(form_obj)