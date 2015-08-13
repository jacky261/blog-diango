# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='headimg',
            field=models.ImageField(upload_to=b'./upload/'),
            preserve_default=True,
        ),
    ]
