# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpletext', '__first__'),
        ('bidders', '0003_bidder_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidder',
            name='tags',
            field=models.ForeignKey(to='simpletext.SimpleCategory', null=True),
        ),
    ]
