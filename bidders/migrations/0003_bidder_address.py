# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidders', '0002_bidder_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidder',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
