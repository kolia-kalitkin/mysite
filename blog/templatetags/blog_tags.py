from django import template
from ..models import Post

register = template.Library()

# шаблонный тег, который возвращает число опубликованных в блоге постов.
@register.simple_tag
def total_posts():
    return Post.published.count()