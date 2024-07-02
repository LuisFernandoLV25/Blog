from django.urls import path
from . import views
urlpatterns = [
    path('',views.starting_page, name="starting-page"),
    path('post',views.post,name="posts-page"),
    path("posts/<slug:slug>",views.post_detail,name="post-detail-page")
]
