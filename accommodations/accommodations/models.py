from django.db import models

class BaseInfo(models.Model):
    """Base class containing all models common information."""

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Define Model as abstract."""

        abstract = True
