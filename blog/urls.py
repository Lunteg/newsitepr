from django.urls import path  
from . import views 
from .views import (
    BlogUpdateView,
    BlogCreateView
) 
  
app_name = 'blog' 
urlpatterns = [ 
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',  
         views.post_single,  
	     name='post_single'), 
]