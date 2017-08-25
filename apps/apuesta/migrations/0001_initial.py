# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=200)),
                ('due_datec', models.DateTimeField(verbose_name='Fecha Limite')),
                ('create_date', models.DateTimeField(verbose_name='Fecha Publicacion', auto_now_add=True)),
                ('update_date', models.DateTimeField(verbose_name='Fecha Actualizada', auto_now_add=True)),
                ('create_user', models.ForeignKey(related_name='pregunta_create_user', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(related_name='pregunta_update_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaValidas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name='Fecha Publicacion', auto_now_add=True)),
                ('update_date', models.DateTimeField(verbose_name='Fecha Actualizada', auto_now_add=True)),
                ('create_user', models.ForeignKey(related_name='respusta_valida_create_user', to=settings.AUTH_USER_MODEL)),
                ('pregunta', models.ForeignKey(to='apuesta.Pregunta')),
                ('update_user', models.ForeignKey(related_name='respusta_valida_update_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='respuestavalidas',
            unique_together=set([('pregunta', 'text')]),
        ),
    ]
