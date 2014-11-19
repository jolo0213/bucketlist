# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blist', '0004_item_finish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bl',
            options={'permissions': (('can_edit', 'can_delete'),)},
        ),
    ]
