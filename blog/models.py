from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')  # поле определяет взаимосвязь многие-к-одному

    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)    # поле даты публикации
    created = models.DateTimeField(auto_now_add=True)       # поле даты создания
    updated = models.DateTimeField(auto_now=True)           # поле даты изменения
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)     # добавим в модель поле статуса, которое позволит управлять статусом постов блога.

    class Meta:
        ordering = ['-publish']     # сортировать результаты по полю publish
        indexes = [
            models.Index(fields=['-publish']),      # опция позволяет определять в модели индексы базы данных, которые могут содержать одно или несколько полей в возрастающем либо убывающем порядке, или функциональные выражения и функции базы данных.
        ]

    def __str__(self):
        return self.title
