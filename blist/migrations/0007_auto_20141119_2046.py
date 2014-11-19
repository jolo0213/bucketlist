# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blist', '0006_auto_20141119_2045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bl',
            options={'permissions': (('can_edit', 'can_delete'),)},
        ),
    ]
