from django.http import Http404
from django.contrib.auth.models import User
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
from .models import (GoogleUser, UserProxy)
from .serializers import (GoogleUserSerializer, UserSerializer)

from .utils import resolve_google_oauth
from .errors import unauthorized


class GoogleRegisterView(APIView):

    permission_classes = (AllowAny,)

    def get_oauth_token(self, userproxy):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        print(api_settings.JWT_PAYLOAD_HANDLER)
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(userproxy)
        token = jwt_encode_handler(payload)

        serializer = UserSerializer(userproxy)

        body = {
            'token': token,
            'user': serializer.data,
        }

        return body

    def post(self, request, format=None):
        
        idinfo = resolve_google_oauth(request)

        try:
            if type(idinfo.data) == type(dict()):
                return Response(idinfo.data)
        except Exception as e:
            pass

        # check if it is a returning user.
        try:
            google_user = GoogleUser.objects.get(google_id=idinfo['sub'])
            google_user.check_diff(idinfo)
            userproxy = UserProxy.objects.get(id=google_user.app_user.id)
            userproxy.check_diff(idinfo)

        except GoogleUser.DoesNotExist:
            # proceed to create the user

            userproxy = UserProxy(
                username=idinfo['name'],
                email=idinfo["email"],
                first_name=idinfo['given_name'],
                last_name=idinfo['family_name']
            )
            userproxy.save()
            google_user = GoogleUser(google_id=idinfo['sub'],
                                     app_user=userproxy,
                                     appuser_picture=idinfo['picture'])
            google_user.save()

        # automatically get token for the created/returning user and log them in:
        body = self.get_oauth_token(userproxy)
        return Response(body, status=status.HTTP_201_CREATED)


class GoogleUserView(GenericAPIView):
    """List Google User by Id."""

    model = GoogleUser
    serializer_class = GoogleUserSerializer

    def get(self, request):
        # import pdb;pdb.set_trace()
        id = self.request.user.id
        app_user = User.objects.get(id=id)
        try:
            google_user = GoogleUser.objects.get(app_user=app_user)
        except GoogleUser.DoesNotExist:
            raise Http404

        serializer = GoogleUserSerializer(google_user)
        return Response(serializer.data)
