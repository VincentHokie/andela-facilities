# resource: https://developers.google.com/identity/sign-in/web/backend-auth
import os

from oauth2client import client, crypt
from rest_framework.response import Response

from .errors import not_allowed, unauthorized


def resolve_google_oauth(request):
    # token should be passed as an object {'ID_Token' : id_token }
    # to this view
    token = request.data.get('ID_Token')
    CLIENT_ID = os.environ.get('CLIENT_ID')

    token.replace(" ", "")

    try:

        # get back user info from google/ throw exception if token is not valid
        idinfo = client.verify_id_token(token, CLIENT_ID)

        # check if user belongs to an organization
        if 'hd' not in idinfo:
            return unauthorized('You don\'t have access to this application')

        # ensure user has a google account
        if idinfo['iss'] not in [
                'accounts.google.com', 'https://accounts.google.com']:
            return unauthorized('Wrong Issuer')

        # user must have an andela mail, have a verified email addressa and
        # the client ID returned by google
        # must match the one in the apps environment variable
        if idinfo['hd'] != 'andela.com' or \
            not idinfo['email_verified'] or \
                idinfo['aud'] != CLIENT_ID:
                return unauthorized('Invalid parameters given')

        # if all the above checks pass, user information
        # is returned for processing
        if idinfo['hd'] == 'andela.com' and \
                idinfo['email_verified'] == True and \
                idinfo['aud'] == CLIENT_ID:
            return idinfo

    # token is not valid and google threw an exception
    except crypt.AppIdentityError:
        return unauthorized('Invalid Token')


    return idinfo
