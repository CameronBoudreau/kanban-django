from django.db import models


class Cards(models.Model):
    title = models.CharField(default='Card', max_length=255)
    description = models.TextField(default='')
    status = models.CharField(default='active', max_length=255)
