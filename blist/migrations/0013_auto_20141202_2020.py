# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blist', '0012_auto_20141201_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bl',
            old_name='name',
            new_name='name',
        ),
    ]
