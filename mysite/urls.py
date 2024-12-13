from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path



sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("accounts/", include("accounts.urls")), 
    path("accounts/", include("django.contrib.auth.urls")),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    
    path("api/", include("blog_api.urls")),
    # # Хорошей практикой является постоянное версионирование API, поскольку при внесении больших изменений может возникнуть некоторая задержка, прежде чем различные потребители API также смогут обновиться. Например создание маршрутов типа:
    # path("api/v1/", include("blog_api_v1.urls")), # API версия 1
    # path("api/v2/", include("blog_api_v2.urls")), # API версия 2

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)