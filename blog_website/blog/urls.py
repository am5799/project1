from django.urls import path
from . import views
from .views import blog_details


urlpatterns = [
    path('users/', views.users, name='users'),
    path('blogs/', views.blogs, name='blogs'),
    path('comments/', views.comments, name='comments'),
    path('categories/', views.categories, name='categories'),
    path('blogdetails/<int:id>/', blog_details, name='blog_details'),
    path('', views.index, name='index'),  # add this line
]
