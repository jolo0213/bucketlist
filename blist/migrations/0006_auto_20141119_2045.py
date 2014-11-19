# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blist', '0005_auto_20141119_2042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bl',
            options={'permissions': (('can_assign', 'can_edit', 'can_delete'),)},
        ),
    ]
