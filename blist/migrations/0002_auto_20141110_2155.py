# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_desc',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='item_url',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
