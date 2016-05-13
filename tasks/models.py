from django.db import models


# class Cards(models.Model):
#     created = models.DateField(auto_now_add=True)
#     title = models.CharField(default='Card', max_length=255)
#     description = models.TextField(default='')
#     status = models.CharField(default='active', max_length=255)
# #
#     class Meta:
#         ordering = ('created', 'status')

class Card(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(default='Card', max_length=255)
    description = models.TextField(default='')
    status = models.CharField(default='active', max_length=255)

    class Meta:
        ordering = ('created', 'status')
