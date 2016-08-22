# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe8\xa6\x81\xe6\xb7\xbb\xe5\x8a\xa0\xe7\x9a\x84\xe7\x9b\xae\xe5\xbd\x95\xe5\x90\x8d\xe7\xa7\xb0', unique=True, max_length=128, verbose_name=b'\xe7\x9b\xae\xe5\xbd\x95\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(help_text=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe8\xa6\x81\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x96\x87\xe7\xab\xa0\xe7\x9a\x84\xe6\xa0\x87\xe9\xa2\x98', max_length=128, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(help_text=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe8\xa6\x81\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x96\x87\xe7\xab\xa0\xe7\x9a\x84URL'),
        ),
    ]
