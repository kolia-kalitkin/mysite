from rest_framework import permissions
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend 


class PostList(generics.ListCreateAPIView):     
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # бэкенд фильтры для нашего представления PostList ()
    filter_backends = [DjangoFilterBackend]     #   появится кнопка Filters
    filterset_fields = ['author']   # набор полей, по которым фильтровать
    # Для более сложных требований к фильтрации вы можете указать класс FilterSet, который должен использоваться представлением.
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAdminUser,)
    

class UserPostList(generics.ListAPIView):
    """представление, которое возвращает набор постов, отфильтрованный по id пользователя в части URL"""
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.kwargs['id']
        return Post.objects.filter(author=user)