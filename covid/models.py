from django.db import models


class Covid19(models.Model):
    covid = models.IntegerField()


class Parser(models.Model):
    corona = models.CharField(max_length=200, default='virus')
