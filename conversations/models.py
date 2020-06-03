from django.db import models
from core import models as core_models


class Conversation(core_models.AbstractTimestamp):

    """ Conversation Model Definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return self.created
