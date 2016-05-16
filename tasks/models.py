from django.db import models

STATUS_CHOICES = ['Urgent', 'In Progress', 'Complete']


class Card(models.Model):
    created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='cards')

    title = models.CharField(default='Card', max_length=255)
    description = models.TextField(default='')
    status = models.CharField(default='active', max_length=255)

    class Meta:
        ordering = ['-status']
