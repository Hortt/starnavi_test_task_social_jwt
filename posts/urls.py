from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.PostListView.as_view(), name='lists_posts'),
    path('<int:pk>/like/', views.PostLikeView.as_view(), name='like_post'),
    path('<int:pk>/unlike/', views.PostUnlikeView.as_view(),
         name='unlike_post'),
    path('', views.PostCreateView.as_view(), name='create_post'),
]
