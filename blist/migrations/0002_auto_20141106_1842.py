# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bucket',
            new_name='BL',
        ),
        migrations.RenameField(
            model_name='bl',
            old_name='list_name',
            new_name='bl_name',
        ),
    ]
