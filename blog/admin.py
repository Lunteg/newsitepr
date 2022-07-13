from django.contrib import admin
from .models import Post, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):  
    list_display = ('title', 'tag', 'author', 'publ_date', 'status')  
    list_filter = ('status', 'creat_date', 'publ_date', 'author')  
    search_fields = ('title', 'body')  
    prepopulated_fields = {'tag': ('title',)}  
    raw_id_fields = ('author', 'category')  
    date_hierarchy = 'publ_date'  
    ordering = ('status', 'publ_date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',) 



