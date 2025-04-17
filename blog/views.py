from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Post


class HomeView(TemplateView):
    template_name = "blog/home.html"

class AboutView(TemplateView):
    template_name = "blog/about.html"


class BloglistView(ListView):
    model = Post
    template_name = "blog/post_list.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = ["title", "text"]  # Don't include 'author'
    success_url = reverse_lazy("blog:post_list")  # Update if needed

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign the logged-in user as author
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ["title", "text"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("blog:post_list")


