# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blist', '0003_auto_20141111_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='finish',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
