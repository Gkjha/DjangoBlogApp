from django.urls import path 
from blog import views
from blog.views import PostDetailView

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about', views.AboutView.as_view(), name='about'),
    path('post/new', views.CreatePostView.as_view(), name='post_new'),
    path('post/draft', views.DraftView.as_view(), name='post_draft_list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', views.UpdatePostView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/comment/publish', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment', views.add_comments, name='add_comment_to_post'),
    path('post/<int:pk>/comment/approve', views.approve_comment, name='comment_approve'),
    path('post/<int:pk>/comment/remove', views.delete_comment, name='comment_remove'),
]
