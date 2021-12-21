# Code copied from Code Institute "I Think Therefore I Blog" project
# on December 20th, 2022 at 17:50 and later modified

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic, View
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )


#class WeatherPageView(generic.TemplateView):
#    template_name = 'weather.html'




#def get_base(request):
#    return render(request, "pp4_ci_wqcs/base.html")
#
#def get_index(request):
#    return render(request, "pp4_ci_wqcs/index.html")
#
#def get_contact(request):
#    return render(request, "pp4_ci_wqcs/contact.html")
#
#def get_weather(request):
#    return render(request, "pp4_ci_wqcs/weather.html")
#
#def get_blog(request):
#    return render(request, "pp4_ci_wqcs/blog.html")