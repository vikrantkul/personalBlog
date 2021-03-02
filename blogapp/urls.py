from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList, name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/base.html', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]