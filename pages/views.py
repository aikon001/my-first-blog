# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Page
from .models import Post

from django.http import HttpResponse
from django.views import generic

# Create your views here.

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'pages/detail.html', {'post': post})
    

def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
        'article_list': Post.objects.all(),
    }
    #assert False
    return render(request,'pages/page.html',context)
