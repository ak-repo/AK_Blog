from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class BloglistView(ListView):
    model = Post
    template_name = "blog/post_list.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = ["title", "author", "text"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ["title", "text"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("post_list")


# from django.shortcuts import render, get_object_or_404

# from .models import Post

# # Create your views here.


# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, "blog/post_list.html", {"posts": posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "blog/post_detail.html", {"post": post})
