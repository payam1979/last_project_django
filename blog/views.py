from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.forms import CommentForm
from django.contrib import messages
from blog.models import Post, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import *

# Create your views here.

def blog_view(request, **kwargs):
   
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude (status= 0)    
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        
    posts = Paginator(posts,3)
    
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)  
    except EmptyPage:
        posts = posts.get_page(1)
        
    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

#def blog_single(request, pid):
    #post = get_object_or_404(Post, pk=pid)
    #context = {'post':post}
    #return render(request, 'blog/single-blog-post.html', context)

def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'we got your comment')
        else:
            messages.add_message(request, messages.ERROR, 'something went wrong')
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude(status= 0)
    post = get_object_or_404(posts,pk=pid)
    comment = Comment.objects.filter(post=post.id, approved=True)
    if request.user.is_authenticated:
        post.counted_view +=1
        post.save()
        post1 = list(posts)
        post2 = list()
        form = CommentForm()        
        for i in range(0,len(post1)):
            if post1[i].id == pid:
                if i == 0:
                    previous_post = post1[i+1]
                        #print(previous_post.id)
                    next_post = post1[0]
                        #print(next_post.id) 
                elif i == len(post1)-1:
                    next_post = post1[i-1]
                        #print(next_post.id)
                    previous_post = post1[len(post1)-1]
                        #print(previous_post.id)
                else:
                    next_post = post1[i-1]
                        #print(next_post.id)  
                    previous_post = post1[i+1]
                        #print(previous_post.id)                        
            #print(next_post, post, previous_post)   
        context = {'post': post,
                        'form': form,
                        'comment': comment,
                        'next': next_post,
                        'previous': previous_post,}
                    
        return render(request, 'blog/single-blog-post.html', context)
    elif not request.user.is_authenticated:
        post.counted_view +=1
        post.save()
        post1 = list(posts)
        post2 = list()
        form = CommentForm()
        if not post.login_require:
            
            for i in range(0,len(post1)):
                if  post1[i].login_require == False:
                    post2.append(post1[i])
           # print(post2)
            for i in range(0,len(post2)):
                if post2[i].id == pid:
                    if i == 0:
                        previous_post = post2[i+1]
                        next_post = post2[0]
                    elif i == len(post2)-1:
                        next_post = post2[i-1]
                        previous_post = post2[len(post2)-1]
                    else:
                        next_post = post2[i-1]
                        previous_post = post2[i+1]
            context = {'post': post,
                            'form': form,
                            'comment': comment,
                            'next': next_post,
                            'previous': previous_post,}
            return render(request, 'blog/single-blog-post.html', context)   
        else:
            return HttpResponseRedirect(reverse('accounts:login'))
        
        
def blog_search(request):
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude (status= 0)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
            count = len(posts)
            if count > 0:
                mes = 'Found' + str(count) + 'posts for your search'
                messages.add_message(request, messages.SUCCESS, mes)
            
            else:
                messages.add_message(request, messages.ERROR, 'Nothing in posts maches your search')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                
    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

