# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page
from .models import Post

#from django_summernote.admin import SummernoteModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.

class PostAdmin(MarkdownModelAdmin):
    list_display = ('title',)

class PageAdmin(MarkdownModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title',)
    

admin.site.register(Page,PageAdmin)
admin.site.register(Post,PostAdmin)
