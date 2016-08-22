# coding: utf-8
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('目录名', max_length=128, unique=True, help_text="请输入要添加的目录名称")
    views = models.IntegerField('访问量', default=0)
    likes = models.IntegerField('点赞量', default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '目录'
        verbose_name_plural = '目录'


class Page(models.Model):
    category = models.ForeignKey(Category, verbose_name='类别')
    title = models.CharField('标题', max_length=128, help_text="请输入要添加文章的标题")
    url = models.URLField(help_text="请输入要添加文章的URL")
    views = models.IntegerField('访问量', default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

