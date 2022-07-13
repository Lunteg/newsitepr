from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Post 
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

# Create your views here.
def post_list(request): 
    page = request.GET.get('page')
    search = request.GET.get('search', '')
    if search != '':
        posts_list = Post.published.filter(category=search)
    else:
        posts_list = Post.published.all() 
        if len(posts_list) > 5:
            posts_list = Post.published.all()[0:5]
            
        
    paginator = Paginator(posts_list, 5)
    try:  
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    categories = Category.objects.all()
    return render(request, 'blog/post/list.html',  
                    {'page': page,  
                   'posts': posts, 
                   'categories' : categories})


def post_single(request, year, month, day, post):  
    post = get_object_or_404(Post, tag=post,  
                 status='published',  
                 publ_date__year=year,  
                 publ_date__month=month,  
                 publ_date__day=day) 
    return render(request,  
          'blog/post/singlepost.html',  
          {'post': post})

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post/post_edit.html'
    fields = ['title', 'body', 'category', 'status'] 

class BlogCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    template_name = 'blog/post/post_new.html'
    fields = ['title', 'body', 'category' ,'status']     
    
    def form_valid(self, form):  
        form.instance.author = self.request.user
        form.instance.tag = slugify(form.instance.title)
        return super().form_valid(form)
