from django.db import models


class AbstractTimestamp(models.Model):

    """ Abstract Timestamp Model """

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True
