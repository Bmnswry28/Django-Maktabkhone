from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.shortcuts import get_object_or_404
def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid, status=1, published_date__lte=timezone.now())
    post.counted_views += 1
    post.save()
    previous_post = Post.objects.filter(published_date__lt=post.published_date, status=True).order_by('-published_date').first()
    next_post = Post.objects.filter(published_date__gt=post.published_date, status=True).order_by('published_date').first()
    context = {'post': post, 'previous_post': previous_post, 'next_post': next_post}
    return render(request, 'blog/blog-single.html', context)