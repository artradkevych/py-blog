from django.shortcuts import redirect
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        content = request.POST.get("content")

        if request.user.is_authenticated and content:
            Commentary.objects.create(
                post=self.object,
                user=request.user,
                content=content
            )

        return redirect("blog:post-detail", pk=self.object.pk)
