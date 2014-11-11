# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blist.models


class Migration(migrations.Migration):

    dependencies = [
        ('blist', '0002_auto_20141110_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='bl',
            name='favorite',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_value',
            field=models.CharField(max_length=200, validators=[blist.models.validate_full]),
            preserve_default=True,
        ),
    ]
