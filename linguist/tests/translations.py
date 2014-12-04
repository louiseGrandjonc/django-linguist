# -*- coding: utf-8 -*_
from django.db import models

from ..base import ModelTranslationBase


class FooModel(models.Model):
    title = models.CharField(max_length=255)


class FooTranslation(ModelTranslationBase):
    model = FooModel
    identifier = 'foo'
    columns = ('title', )


class BarModel(models.Model):
    title = models.CharField(max_length=255)


class BarTranslation(ModelTranslationBase):
    model = BarModel
    identifier = 'bar'
    columns = ('title', )


class BadTranslation(object):
    pass


class BadModel(object):
    pass
