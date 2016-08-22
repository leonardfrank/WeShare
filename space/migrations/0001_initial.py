# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, verbose_name=b'\xe7\x9b\xae\xe5\xbd\x95\xe5\x90\x8d')),
                ('views', models.IntegerField(default=0, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe9\x87\x8f')),
                ('likes', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe8\xb5\x9e\xe9\x87\x8f')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': '\u76ee\u5f55',
                'verbose_name_plural': '\u76ee\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe9\x87\x8f')),
                ('category', models.ForeignKey(verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab', to='space.Category')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
