from django.shortcuts import render

from .models import Post

# Create your views here.

def post_list_view(request):
    post_objects = Post.objects.all()
    context = {
        'post_objects': post_objects
    }

    return render(request, "posts/all.html", context)

def post_detail_view(request, detail_id):
    post_object = Post.objects.get(id=detail_id)
    context = {
        'post_object': post_object

    }

    return render(request, "posts/detail.html", context)