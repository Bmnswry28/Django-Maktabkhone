from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.shortcuts import get_object_or_404
def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request, pid):
    post = get_object_or_404(
        Post,
        id=pid,
        status=1,  
        published_date__lte=timezone.now()
    )

    post.counted_view += 1
    post.save()

    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)