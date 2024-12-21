from django.urls import path, re_path
from .views import PostList, PostDetail, UserPostList
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView 

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),    
    re_path('^user/(?P<id>.+)/$', UserPostList.as_view()),
    
    # предоставлении схемы непосредственно из нашего API в виде URL-маршрута (динамический подход)
    #  Автоматически сгенерированный файл схемы всего нашего API доступен и будет загружен в виде файла.
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    
    # В drf-spectacular поддерживаются два инструмента документирования API: Redoc и SwaggerUI.
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),


]