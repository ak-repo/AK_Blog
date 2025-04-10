from .models import Post


def recent_posts_processor(request):
    recent_posts = Post.objects.order_by("-created_date")[:5]
    return {"posts": recent_posts}
