# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Pregunta(models.Model):
    text = models.CharField(max_length=200)
    due_date = models.DateTimeField('Fecha Limite')
    create_date = models.DateTimeField('Fecha Publicacion', auto_now_add=True)
    create_user = models.ForeignKey(User, related_name="pregunta_create_user")
    update_date = models.DateTimeField('Fecha Actualizada', auto_now_add=True)
    update_user = models.ForeignKey(User, related_name="pregunta_update_user")

    def __unicode__(self):
        return "%s" % (self.text)

    @property
    def respuestas_validas(self):
        return RespuestaValidas.objects.filter(pregunta=self)


class RespuestaValidas(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    create_date = models.DateTimeField('Fecha Publicacion', auto_now_add=True)
    create_user = models.ForeignKey(User, related_name="respusta_valida_create_user")
    update_date = models.DateTimeField('Fecha Actualizada', auto_now=True)
    update_user = models.ForeignKey(User, related_name="respusta_valida_update_user")


    class Meta:
        unique_together = ('pregunta', 'text')

    def __unicode__(self):
        return "%s" % (self.text)


class Apuestas(models.Model):
    pregunta = models.ForeignKey(Pregunta, blank=True, null=True)
    respuesta_valida = models.ForeignKey(RespuestaValidas)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'pregunta')

    def __unicode__(self):
        return "[%s], %s" % (self.respuesta_valida.pregunta, self.user)

    def save(self, *args, **kwargs):
        self.pregunta = self.respuesta_valida.pregunta
        return super(Apuestas, self).save(*args, **kwargs)
