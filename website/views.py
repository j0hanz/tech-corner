from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    template_name = "website/index.html"
    paginate_by = 6
    ordering = ["-created_on"]


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(
        request, "website/post_detail.html", {"post": post}
    )
