from django.http import Http404

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    get_object_or_404
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Like, Post
from .permissions import ObjectAuthorPermission
from .serializers import (
    PostInputSerializer,
    PostLikeSerializer,
    PostOutputSerializer
)


class PostCreateView(CreateAPIView):

    serializer_class = PostInputSerializer
    permission_classes = (IsAuthenticated,)


class PostListView(ListAPIView):

    serializer_class = PostOutputSerializer
    queryset = Post.objects.all().prefetch_related('like_set')
    permission_classes = (AllowAny, )


class PostLikeView(CreateAPIView):

    serializer_class = PostLikeSerializer
    permission_classes = (IsAuthenticated, ObjectAuthorPermission,)

    def create(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        request.data.update({'post': post})
        return super().create(request, *args, **kwargs)


class PostUnlikeView(DestroyAPIView):

    serializer_class = PostLikeSerializer
    permission_classes = (IsAuthenticated, ObjectAuthorPermission,)

    def get_object(self, queryset=None):
        latest_like = Like.objects.filter(
            author=self.request.user,
            post_id=self.kwargs['pk']).last()
        if not latest_like:
            raise Http404
        return latest_like
