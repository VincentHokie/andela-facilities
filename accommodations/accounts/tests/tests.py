from django.test import TestCase
from django.contrib.auth.models import Group

# Create your tests here.
class BaseAccountSetup():

    def create_groups(self):
        group = Group(name='Fellow')
        group.save()

        group = Group(name='FellowOccupant')
        group.save()

        group = Group(name='PNC')
        group.save()

        group = Group(name='FacilitiesAdmin')
        group.save()

        group = Group(name='Finance')
        group.save()
