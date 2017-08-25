# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuesta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pregunta',
            old_name='due_datec',
            new_name='due_date',
        ),
    ]
