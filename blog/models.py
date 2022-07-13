from unicodedata import category
from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone 
from django.urls import reverse

# Create your models here.
class PublishedManager(models.Manager):  
    def get_queryset(self):  
        return super(PublishedManager,  
		     self).get_queryset().filter(status='published')

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self): 
        return self.name   

class Post(models.Model):
    title = models.CharField(max_length=250)
    tag = models.SlugField(max_length=250, 
                            unique_for_date='publ_date')
    category = models.ForeignKey(Category, 
                                on_delete=models.CASCADE)
    body = models.TextField()                       
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE, 
                               related_name='blog_posts')       
    publ_date = models.DateTimeField(default=timezone.now)
    creat_date = models.DateTimeField(auto_now_add=True)  
    upd_date = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    )
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES, 
                              default='draft')
    objects = models.Manager()  # Менеджер по умолчанию  
    published = PublishedManager()  # Собственный менеджер
    
    class Meta: 
        ordering = ('-publ_date',) 

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self):  
        return reverse('blog:post_single',  
		       args=[self.publ_date.year,  
                    self.publ_date.month,  
                    self.publ_date.day,  
                    self.tag])

