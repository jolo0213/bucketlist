# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blist', '0010_auto_20141119_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='finish',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
