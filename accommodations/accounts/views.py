from django.http import Http404
from django.contrib.auth.models import User, Group
from django.urls import reverse

from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView
from rest_framework.views import APIView

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .setpagination import LimitOffsetpage
from .models import User
from .serializers import UserSerializer

from .utils import resolve_google_oauth
from .errors import unauthorized


class GoogleRegisterView(APIView):

    permission_classes = (AllowAny,)
    authentication_classes = []

    def get_oauth_token(self, user):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        serializer = UserSerializer(user)

        body = {
            'token': token,
            'user': serializer.data,
        }

        return body

    def post(self, request, format=None):

        # pass token to get google info/ an error if the checks dont pass
        idinfo = resolve_google_oauth(request)

        if isinstance(idinfo, Response):
            return idinfo

        # check if it is a returning user.
        try:
            user = User.objects.get(google_id=idinfo['sub'])
            user.check_diff(idinfo)

        except User.DoesNotExist:
            # proceed to create the user

            user = User(
                username=idinfo['name'],
                email=idinfo["email"],
                first_name=idinfo['given_name'],
                last_name=idinfo['family_name'],
                google_id=idinfo['sub'],
                appuser_picture=idinfo['picture']
            )
            user.save()

            # ensure every new user is given the least rights i.e.
            # those of a fellow
            my_group = Group.objects.get(name='Fellow')
            my_group.user_set.add(user)

        # automatically get token for the created/returning
        # user and log them in:
        body = self.get_oauth_token(user)
        return Response(body, status=status.HTTP_201_CREATED)


class GoogleUserView(GenericAPIView):
    """List Google User by Id."""

    model = User
    serializer_class = UserSerializer

    def get(self, request):
        id = self.request.user.id
        app_user = User.objects.get(id=id)
        serializer = UserSerializer(app_user)
        return Response(serializer.data)
