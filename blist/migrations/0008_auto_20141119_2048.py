# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blist', '0007_auto_20141119_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bl',
            options={'permissions': (('can_assign', 'List owner that can change who can edit/delete the list'), ('can_delete', 'User who can delete the list'), ('can_edit', 'User who can change list items'))},
        ),
    ]
