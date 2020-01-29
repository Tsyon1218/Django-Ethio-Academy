from django.shortcuts import render
from .models import Post
def Blog(request):
    all_blogs = Post.objects.all()
    context = {"all_blogs":all_blogs }
    return render(request, 'Blog/Blog.html',context)
def detail(request,blog_id):
    single_blog = Blog.objects.get(id=blog_id )
    context = {"single_blog":single_blog }
    return render(request, 'Blog/detail.html',context)

