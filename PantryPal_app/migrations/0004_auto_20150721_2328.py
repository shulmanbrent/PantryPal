# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PantryPal_app', '0003_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='query',
            name='user',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
