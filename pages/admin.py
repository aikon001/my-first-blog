# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page

from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
class PageAdmin(MarkdownModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title',)
    #formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(Page,PageAdmin)
