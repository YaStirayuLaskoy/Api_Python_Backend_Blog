# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group, Comment, Follow, User
from .serializers import PostSerializer, GroupSerializer, UserSerializer
from .serializers import CommentSerializer, FollowSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет юзера."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    # Пагинация
    pagination_class = LimitOffsetPagination

    # Фильтрация, сортировка и поиск
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    filterset_fields = ('author', 'group')
    search_fields = ('author', 'group')
    ordering_fields = ('__all__')
    ordering = ('pub_date',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    # Пагинация
    pagination_class = LimitOffsetPagination


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет комментов."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    # Пагинация
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        return post.comments


class FollowViewSet(viewsets.ModelViewSet):
    """Вьюсет подписки."""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        """Возвращает все подписки пользователя, сделавшего запрос"""
        new_queryset = Follow.objects.filter(user=self.request.user)
        return new_queryset

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
