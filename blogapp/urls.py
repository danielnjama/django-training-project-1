from django.urls import path
from . import views

urlpatterns = [ 
    path('blog/',views.blog,name='blog'),
    path('post/<slug:url>', views.post_detail, name='postdetail'),
    path('category/<slug:category_slug>/', views.post_list_by_category, name='post_list_by_category'),
   
]