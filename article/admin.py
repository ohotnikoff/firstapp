# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article.models import Article, Comment

class ArticleInline(admin.StackedInline):
    model = Comment
    extra = 2
class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_anons', 'article_text', 'article_date']
    inlines = [ArticleInline]
    list_filter = ['article_date']

# Register your models here.
admin.site.register(Article, ArticleAdmin)