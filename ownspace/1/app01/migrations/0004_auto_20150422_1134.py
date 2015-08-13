# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20150422_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='headimg',
            field=models.ImageField(upload_to=b'/upload/image/'),
            preserve_default=True,
        ),
    ]
