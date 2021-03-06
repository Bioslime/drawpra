from django.urls import path

from . import views

app_name = "menu"
urlpatterns =[
    path("pictform/", views.PictFormView.as_view(), name="pictform"),
    path("top/",views.Top.as_view(), name="top" ),
    path("postlist/", views.PostLsit.as_view(), name="postlist"),
    path("postdelete/<uuid:pk>", views.PostDeleteView.as_view(), name="postdelete"),
    path("goodpointform/", views.GoodPointFormview.as_view(), name="goodpointform"),
    path("postdetail/<uuid:pk>", views.PictDetailGoodPost.as_view(), name="postdetail"),
    path("goodpointdetail/<uuid:pk>", views.GoodPointDetail.as_view(),name="goodpointdetail"),
    path("GPdelete/<uuid:pk>", views.GPDeleteView.as_view(), name="GPdelete"),
]