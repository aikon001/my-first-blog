# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True,null=True)
    image = models.FileField(upload_to='images',blank=True)
    slug = models.SlugField(blank=True, default='') 

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12,unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.title
