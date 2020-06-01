from django.db import models


class AbstractTimestamp(models.Model):

    """ Abstract Timestamp Model """

    created = models.DateField()
    updated = models.DateField()

    class Meta:
        abstract = True
