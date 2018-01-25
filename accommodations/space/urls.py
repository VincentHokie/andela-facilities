from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    ViewSpace, UpdateDeleteSpace, CreateSpace, ViewOccupant,
    UpdateOccupant, DeleteOccupant, CreateOccupant,
    ViewRoom, UpdateRoom, DeleteRoom, CreateRoom, RetrieveSpace,
    RetrieveRoom, RetrieveOccupant
)


urlpatterns = {

    ###################################
    #
    #   CRD urls for the space model
    #
    ###################################

    url(
        r'^space/$',
        ViewSpace.as_view(), name='view-accomodation-space'),
    url(
        r'^space/create/$',
        CreateSpace.as_view(), name="create-accomodation-space"),
    url(
        r'^space/(?P<pk>[0-9]+)/$',
        UpdateDeleteSpace.as_view(),
        name="update-accomodation-space"),
    url(
        r'^space/(?P<pk>[0-9]+)$',
        RetrieveSpace.as_view(),
        name="retrieve-accomodation-space"),


    ###################################
    #
    #   CRD urls for the room model
    #
    ###################################
    url(
        r'^(?P<space_id>[0-9]+)/room/$',
        ViewRoom.as_view(), name='view-accomodation-room'),
    url(
        r'^(?P<space_id>[0-9]+)/room/create/$',
        CreateRoom.as_view(), name="create-accomodation-room"),
    url(
        r'^(?P<space_id>[0-9]+)/room/(?P<room_id>[0-9]+)/update/$',
        UpdateRoom.as_view(),
        name="update-accomodation-room"),
    url(
        r'^(?P<space_id>[0-9]+)/room/(?P<room_id>[0-9]+)/delete/',
        DeleteRoom.as_view(),
        name="delete-accomodation-room"),
    url(
        r'^(?P<space_id>[0-9]+)/room/(?P<room_id>[0-9]+)/$',
        RetrieveRoom.as_view(),
        name="retrieve-accomodation-room"),


    ###################################
    #
    #   CRD urls for the occupant model
    #
    ###################################
    url(
        r'^(?P<room_id>[0-9]+)/occupant/$',
        ViewOccupant.as_view(), name='view-room-occupant'),
    url(
        r'^(?P<room_id>[0-9]+)/occupant/create/$',
        CreateOccupant.as_view(),
        name="create-room-occupant"),
    url(
        r'^(?P<room_id>[0-9]+)/occupant/(?P<occupant_id>[0-9]+)/update/$',
        UpdateOccupant.as_view(),
        name="update-room-occupant"),
    url(
        r'^(?P<room_id>[0-9]+)/occupant/(?P<occupant_id>[0-9]+)/delete/$',
        DeleteOccupant.as_view(),
        name="delete-room-occupant"),
    url(
        r'^(?P<room_id>[0-9]+)/occupant/(?P<occupant_id>[0-9]+)/$',
        RetrieveOccupant.as_view(),
        name="retrieve-room-occupant"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
