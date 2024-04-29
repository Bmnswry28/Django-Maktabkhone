from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request, pid):
    return render(request ,'blog/blog-single.html') 