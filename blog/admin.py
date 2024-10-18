from django.contrib import admin
from .models import Post
from .models import Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']     # отображаемые на странице списка постов поля
    list_filter = ['status', 'created', 'publish', 'author']     # страница списка содержит правую боковую панель, которая позволяет фильтровать результаты по полям, включенным в атрибут list_filter
    search_fields = ['title', 'body']   # определили список полей, по которым можно выполнять поиск
    prepopulated_fields = {'slug': ('title',)}   # сообщили Django, что нужно предзаполнять поле slug данными, вводимыми в поле title
    raw_id_fields = ['author']   # поле author отображается поисковым виджетом, который будет более приемлемым, чем выбор из выпадающего списка, когда у вас тысячи пользователей.
    autocomplete_fields = ['author']   # autocomplete_fields  - заменяет выпадающий список на поле с автозаполнением,
    date_hierarchy = 'publish'   # навигационные ссылки для навигации по иерархии дат
    ordering = ['status', 'publish']   # по умолчанию посты упорядочены по столбцам 'status', 'publish'