# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"
    article_title = models.CharField(max_length=200, verbose_name="Заголовок")
    article_anons = models.TextField(verbose_name="Анонс статьи")
    article_text = RichTextField(verbose_name="Текст статьи")
    article_date = models.DateTimeField(verbose_name="Дата публикации")
    article_likes = models.IntegerField(default=0)

class Comment(models.Model):
    class Meta:
        db_table = "comment"
    comment_text = models.TextField(verbose_name="Комментарий")
    comment_article = models.ForeignKey(Article)