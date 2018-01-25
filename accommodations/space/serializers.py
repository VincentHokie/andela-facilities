from .models import Space, Room, Occupant
from rest_framework import serializers


class SpaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Space
        fields = ("id", "space_name", "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified")


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = (
            "id", "space", "room_name", "capacity",
            "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified")


class OccupantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Occupant
        fields = (
            "id", "room", "user", "entry_date", "exit_date",
            "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified")
