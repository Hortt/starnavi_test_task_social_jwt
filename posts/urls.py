from django.conf.urls import url

from . import views


urlpatterns = [
    url('list/', views.PostListView.as_view(), name='lists_posts'),
    url('(?P<pk>[0-9+]+)/like/', views.PostLikeView.as_view(),
        name='like_post'),
    url('(?P<pk>[0-9+]+)/unlike/', views.PostUnlikeView.as_view(),
        name='unlike_post'),
    url('', views.PostCreateView.as_view(), name='create_post'),
]
