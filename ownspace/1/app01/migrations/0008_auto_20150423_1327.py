# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20150423_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='headimg',
            field=models.ImageField(default=b'imgage/commm.jpg', upload_to=b'image/'),
            preserve_default=True,
        ),
    ]
