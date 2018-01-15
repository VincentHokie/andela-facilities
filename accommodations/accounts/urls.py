# resources: https://getblimp.github.io/django-rest-framework-jwt/
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from accounts import views


from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token


urlpatterns = [
    url(r'^user/$', views.GoogleUserView.as_view(),
        name='app_user'),

    url(r'^auth/register/$', views.GoogleRegisterView.as_view(),
        name='auth_register'),

    url(r'^auth/refresh/$', refresh_jwt_token,
        name='auth_refresh'),

    url(r'^auth/verify/$', verify_jwt_token,
        name='auth_verify'),
]


urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
