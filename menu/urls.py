from django.urls import path

from . import views

app_name = "menu"
urlpatterns =[
    path("formtest/", views.PictFormView.as_view(), name="formtest"),
    path("top/",views.Top.as_view(), name="top" ),
    path("postlist/", views.PostLsit.as_view(), name="postlist"),
]