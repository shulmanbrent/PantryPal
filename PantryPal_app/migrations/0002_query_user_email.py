# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PantryPal_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='user_email',
            field=models.CharField(default='unknown', max_length=75),
            preserve_default=False,
        ),
    ]
