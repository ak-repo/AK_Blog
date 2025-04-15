from django.urls import path

from . import views


# app_name = "blog"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("posts/", views.BloglistView.as_view(), name="post_list"),
    path("posts/new/", views.BlogCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/", views.BlogDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", views.BlogUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="post_delete"),
]
