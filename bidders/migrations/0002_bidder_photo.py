# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('bidders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidder',
            name='photo',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.Image', help_text='\uc0ac\uc9c4 \ucd94\uac00', null=True),
        ),
    ]
