from django.urls import path

from . import views

app_name = "menu"
urlpatterns =[
    path("formtest/", views.PictFormView.as_view(), name="formtest"),
    path("test/", views.TestFormView.as_view(),  name="test"),
    path("testlist/", views.TestListView.as_view(), name="testlist"),
    path("testdetail/<uuid:pk>/", views.TestDetailView.as_view(), name="testdetail"),
]