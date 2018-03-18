# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.contrib import auth
from article.models import Article, Comment
from article.forms import CommentForm

# Create your views here.
def basic_one(request):
    view = 'basic_one'
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)

def template_two(request):
    view = 'template_two'
    html = get_template('myview.html').render({'name': view})
    return HttpResponse(html)

def template_three_simple(request):
    view = 'template_three'
    return render_to_response('myview.html', {'name': view})

def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 2)
    return render(request, 'article/articles.html', {
        'articles': current_page.page(page_number),
        'username': auth.get_user(request).username
    })

def article(request, article_id=1):
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comment.objects.filter(comment_article_id=article_id)
    args['form'] = CommentForm
    args['username'] = auth.get_user(request).username
    return render(request, 'article/article.html', args)

def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)