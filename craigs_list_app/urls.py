from django.contrib import admin
from django.urls import path, include
from craigs_list_app import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:category_id>", views.category_detail, name="category_detail"),
    path("<int:category_id>/posts", views.post_list, name="post_list"),
    path("<int:category_id>/posts/new", views.post_new, name="post_new"),
]