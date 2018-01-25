from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    """
    Custom exception handler for Django Rest Framework that adds
    the `status_code` to the response and renames the `detail` key to `error`.
    """
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['error'] = response.data['detail']
        del response.data['detail']

    body = {
        'status': response.data['status_code'],
        'error': response.data['error']}

    return Response(body, status=response.data['status_code'])
