""" """
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import QueryDict
from accommodations.permissions import (IsFacilitiesManager)
from space.serializers import (
    OccupantSerializer, RoomSerializer, SpaceSerializer)
from space.models import (Space, Room, Occupant)


###################################
#
#   CRD views for the space model
#
###################################

class SpaceCRUD(generics.GenericAPIView):
    """
    This class defines common variables for Space crud views
    """
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer


class ViewSpace(
        SpaceCRUD,
        mixins.ListModelMixin):
    """
    This class defines the view behaviour on the Space model
    """
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = "pk"

    def get(self, request, *args, **kwargs):
        """
            handle request with get method
        """
        return self.list(request, *args, **kwargs)


class RetrieveSpace(
        SpaceCRUD,
        mixins.RetrieveModelMixin):
    """
    This class defines the retrieve behaviour on the Space model
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
            handle request with get method
        """
        return self.retrieve(request, *args, **kwargs)


class CreateSpace(
        SpaceCRUD,
        mixins.CreateModelMixin):
    """
    This class defines the create behaviour on the Space model
    """
    permission_classes = (IsAuthenticated, IsFacilitiesManager)

    def post(self, request, *args, **kwargs):
        """
            handle request with post method
        """
        return self.create(request, *args, **kwargs)


class UpdateDeleteSpace(
        SpaceCRUD, mixins.DestroyModelMixin,
        mixins.UpdateModelMixin):
    """
    This class defines the update and delete behaviour on the Space model
    """
    permission_classes = (IsAuthenticated, IsFacilitiesManager)

    def delete(self, request, *args, **kwargs):
        """
            handle request with delete method
        """
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
            handle request with put method
        """
        return self.update(request, *args, **kwargs)


###################################
#
#   CRD views for the room model
#
###################################


class RoomCrud(generics.GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg_room = "room_id"
    lookup_url_kwarg_space = "space_id"


class RoomGetObjectAbstract(RoomCrud):

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        filter_kwargs = {
            "space": self.kwargs[self.lookup_url_kwarg_space],
            "id": self.kwargs[self.lookup_url_kwarg_room]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj


class ViewRoom(
        mixins.ListModelMixin,
        RoomCrud):
    """
    This class defines the view behaviour on the Room model
    """
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        space = self.kwargs.get(self.lookup_url_kwarg_space)
        rooms = Room.objects.filter(space=space)
        return rooms

    def get(self, request, *args, **kwargs):
        """
            handle request with get method
        """
        return self.list(request, *args, **kwargs)


class RetrieveRoom(
        mixins.RetrieveModelMixin,
        RoomGetObjectAbstract):
    """
    This class defines the retrieve behaviour on the Room model
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
            handle request with get method
        """
        return self.retrieve(request, *args, **kwargs)


class CreateRoom(
        mixins.CreateModelMixin,
        RoomCrud):
    """
    This class defines the create behaviour on the Room model
    """
    permission_classes = (IsAuthenticated, IsFacilitiesManager)

    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):

        # add url parameter to the request object being serialized
        space = self.kwargs.get(self.lookup_url_kwarg_space)

        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data["space"] = space

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED,
            headers=headers)

    def post(self, request, *args, **kwargs):
        """
            handle request with post method
        """
        return self.create(request, *args, **kwargs)


class UpdateRoom(
        mixins.UpdateModelMixin,
        RoomGetObjectAbstract):
    """
    This class defines the update behaviour on the Room model
    """
    permission_classes = (IsAuthenticated, IsFacilitiesManager)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # append url parameter information into request data for validation
        if isinstance(request.data, QueryDict):
            request.data._mutable = True

        request.data["id"] = self.kwargs[self.lookup_url_kwarg_room]
        request.data["space"] = self.kwargs[self.lookup_url_kwarg_space]

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        """
            handle request with put method
        """
        return self.update(request, *args, **kwargs)


class DeleteRoom(
        mixins.DestroyModelMixin,
        RoomGetObjectAbstract):
    """
    This class defines the delete behaviour on the Room model
    """
    permission_classes = (IsAuthenticated, IsFacilitiesManager)

    def delete(self, request, *args, **kwargs):
        """
            handle request with delete method
        """
        return self.destroy(request, *args, **kwargs)


###################################
#
#   CRD views for the occupant model
#
###################################

class OccupantAbstract(generics.GenericAPIView):
    queryset = Occupant.objects.all()
    serializer_class = OccupantSerializer
    lookup_url_kwarg_room = "room_id"
    lookup_url_kwarg_occupant = "occupant_id"


class OccupantGetObjectAbstract(OccupantAbstract):

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        filter_kwargs = {
            "id": self.kwargs[self.lookup_url_kwarg_occupant],
            "room_id": self.kwargs[self.lookup_url_kwarg_room]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj


class ViewOccupant(
        mixins.ListModelMixin, OccupantAbstract):
    """
    This class defines the create behaviour of our rest api
    """
    permission_classes = (IsAuthenticated, IsFacilitiesManager)

    def get_queryset(self):
        room = self.kwargs.get(self.lookup_url_kwarg_room)
        occupants = Occupant.objects.filter(room=room)
        return occupants

    def get(self, request, *args, **kwargs):
        """
            handle request with get method
        """
        return self.list(request, *args, **kwargs)


class RetrieveOccupant(
        mixins.RetrieveModelMixin, OccupantGetObjectAbstract):
    """
    This class defines the retrieve behaviour on the Occupant model
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
            handle request with get method
        """
        return self.retrieve(request, *args, **kwargs)


class CreateOccupant(
        mixins.CreateModelMixin, OccupantAbstract):
    """
    This class defines the create behaviour on the Occupant model
    """
    permission_classes = (IsAuthenticated, IsFacilitiesManager)

    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):

        # add url parameter to the request object being serialized
        room = self.kwargs.get(self.lookup_url_kwarg_room)

        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data["room"] = room

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED,
            headers=headers)

    def post(self, request, *args, **kwargs):
        """
            handle request with post method
        """
        return self.create(request, *args, **kwargs)


class UpdateOccupant(
        mixins.UpdateModelMixin, OccupantGetObjectAbstract):
    """
    This class defines the update behaviour on the Occupant model
    """
    permission_classes = (IsAuthenticated, IsFacilitiesManager)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # append url parameter information into request data for validation
        if isinstance(request.data, QueryDict):
            request.data._mutable = True

        request.data["id"] = self.kwargs[self.lookup_url_kwarg_occupant]
        request.data["room"] = self.kwargs[self.lookup_url_kwarg_room]

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        """
            handle request with a put method
        """
        return self.update(request, *args, **kwargs)


class DeleteOccupant(
        mixins.DestroyModelMixin, OccupantGetObjectAbstract):
    """
    This class defines the delete behaviour on the Occupant model
    """
    permission_classes = (IsAuthenticated, IsFacilitiesManager)

    def delete(self, request, *args, **kwargs):
        """
            handle request with delete a method
        """
        return self.destroy(request, *args, **kwargs)
