from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from accommodations.models import BaseInfo


class Space(BaseInfo):

    """
        Stores information about andela spaces i.e Apartment 1, St C
    """
    space_name = models.CharField(max_length=200, unique=True)

    class Meta:
        """Define odering below."""

        ordering = ['space_name']

    def __unicode__(self):
        return "Space Name: {}" .format(self.space_name)


class Room(BaseInfo):
    """
        Stores information about a room in a space ie name, capacity
    """
    space = models.ForeignKey(
        Space, related_name="space", on_delete=models.CASCADE)
    room_name = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        """Deifne unique coupled field"""

        unique_together = ('space', 'room_name',)

    def __unicode__(self):
        return "Room Name: {}" .format(self.room_name + " in " + self.space)


class Occupant(BaseInfo):
    """
        Stores information about an occupant in an andela space
    """
    room = models.ForeignKey(
        Room, related_name="room", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="room")
    entry_date = models.DateField()
    exit_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return "Occupant: {}" .format(self.user + " in " + self.room)
