from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/latest_posts.html')
def latest_blog_posts(count=6):
    latest_posts = Post.objects.order_by('-pub_date')[:count]
    print(latest_posts) 
    return {'latest_posts': latest_posts}