# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-17 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_book_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='notes',
        ),
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='no value'),
            preserve_default=False,
        ),
    ]
