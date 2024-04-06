from django import template
from blog.models import Post, Comment
from django.utils import timezone
from blog.models import Category


register = template.Library()

@register.simple_tag(name='posts')
def numeric():
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude (status= 0)
    return posts

@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid, approved=True).count()

@register.filter
def snippet(value, arg=20):
    return value[:arg]+'...'

@register.inclusion_tag('blog/blog-latest.html')
def latestposts(arg=1):
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude (status= 0)[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-popular.html')
def popularpost(arg=4):
    posts1 = Post.objects.filter(status= 1).order_by('-counted_view')[:arg]
    return {'posts1': posts1}

@register.inclusion_tag('blog/blog-post-categories.html')
def categories():
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude (status= 0)
    categories=Category.objects.all()
    cat_dict={}
    for name in categories:
        
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories': cat_dict}    
        
