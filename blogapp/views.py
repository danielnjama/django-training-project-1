from django.shortcuts import render, redirect, get_object_or_404
from . models import Category,Tag,Post,Comment
from django.db import models
from django.http import Http404

# Create your views here.
def blog(request):
    blogposts = Post.objects.filter(published = True)
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
    blog_tags = Tag.objects.all()
    
    #recent blogs
    recent_posts = Post.objects.order_by('-created_at')[:5]
    context = {"blogposts": blogposts,'blog_categories':blog_categories,'blog_tags':blog_tags,'recent_posts':recent_posts}
    
    return render(request,'blog.html',context)


def post_list_by_category(request, category_slug):
    try:
        #fetch and count blog categories
        blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
        
        #fetch tags
        blog_tags = Tag.objects.all()
        
        #recent blogs
        recent_posts = Post.objects.order_by('-created_at')[:5]
        
        # Retrieve the category object based on the slug
        selected_blog_categories = Category.objects.get(url=category_slug)
        
        
        # Retrieve all posts belonging to the specified category
        blogposts = Post.objects.filter(categories=selected_blog_categories, published=True)
        
        context = {"blogposts": blogposts,'blog_categories':blog_categories,'blog_tags':blog_tags,'recent_posts':recent_posts}
       
        return render(request, 'blog.html', context)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")


def post_detail(request,url):
    post = get_object_or_404 (Post, url=url)
    approved_blogs = Post.objects.filter(published=True)
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
    #recent blogs
    recent_posts = Post.objects.order_by('-created_at')[:5] 
    comments = post.comment_set.filter(approved=True)
    

    context = {'post':post,'blogs': approved_blogs,'blog_categories':blog_categories,'recent_posts':recent_posts,'comments':comments}
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     message = request.POST['message']
    #     comment_instance = Comment(name=name,email=email,message=message,blog=post)
    #     comment_instance.save()
    #     return redirect('postdetail',url=url)
    return render(request,'single.html',context)


