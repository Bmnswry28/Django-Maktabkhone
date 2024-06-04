from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('website/latest_posts.html')
def latest_posts(num=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:num]
    return {'posts': posts}