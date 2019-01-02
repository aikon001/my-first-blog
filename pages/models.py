# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12,unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.title
