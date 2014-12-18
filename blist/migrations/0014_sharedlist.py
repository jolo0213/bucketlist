# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blist', '0013_auto_20141202_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('bucket', models.ForeignKey(to='blist.BL')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
