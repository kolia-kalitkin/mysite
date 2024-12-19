from rest_framework import permissions
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend 
# from rest_framework.views import APIView

# class MyView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     # ... ваш код ...


class PostList(generics.ListCreateAPIView):     
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # бэкенд фильтры для нашего представления PostList
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['author']

    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserPostList(generics.ListAPIView):
    """представление, которое возвращает набор постов, отфильтрованный по id пользователя в части URL"""
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.kwargs['id']
        return Post.objects.filter(author=user)