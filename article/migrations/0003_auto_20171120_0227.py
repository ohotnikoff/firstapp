# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 21:27
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20171114_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_anons',
            field=models.TextField(default='', verbose_name='\u0410\u043d\u043e\u043d\u0441 \u0441\u0442\u0430\u0442\u044c\u0438'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u0442\u0430\u0442\u044c\u0438'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=200, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439'),
        ),
    ]
