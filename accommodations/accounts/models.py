from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProxy(User):
    """Class defined to create a proxy for the user model.

        Changes made to this model directly affects the User model
        and vice-versa. Model allows methods to be defined on the User model
        without altering the user model itself.
        https://docs.djangoproject.com/en/1.11/topics/db/models/
    """
    class Meta:
        proxy = True
        auto_created = True

    def check_diff(self, idinfo):
        """
        Check for differences between request/idinfo and model data.

            Args:
                idinfo: data passed in from post method.
        """
        data = {
                "username": idinfo['name'],
                "email" : idinfo["email"],
                "first_name" :idinfo['given_name'],
                "last_name" :idinfo['family_name']
            }
            
        for field in data:
            if getattr(self, field) != data[field] and data[field] != '':
                setattr(self, field, data[field])
        self.save()


class GoogleUser(models.Model):
    google_id = models.CharField(max_length=60, unique=True)

    app_user = models.OneToOneField(User, related_name='user',
                                    on_delete=models.CASCADE)
    appuser_picture = models.TextField()


    def check_diff(self, idinfo):
        """Check for differences between request/idinfo and model data.
            Args:
                idinfo: data passed in from post method.
        """
        data = {
                "appuser_picture": idinfo['picture']
            }

        for field in data:
            if getattr(self, field) != data[field] and data[field] != '':
                setattr(self, field, data[field])
        self.save()


    def __unicode__(self):
        return "%s %s" % (self.app_user.first_name,
                          self.app_user.last_name)