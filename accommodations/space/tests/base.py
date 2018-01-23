"""This module imports django test configuration"""
from django.test import TestCase

from django.contrib.auth.models import Group
from accounts.models import User
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from accounts.tests.tests import BaseAccountSetup

# Create your tests here.
class BaseTestCase(TestCase, BaseAccountSetup):
    """
        Class that sets up the different users, groups and creates
        test data used by tests in the space app
    """
    def add_to_group(self, group, user):
        """
            adds the provided user to the provided group

            :group: the group to add the user to
            :user: the user to add to the group
        """
        my_group = Group.objects.get(name=group)
        my_group.user_set.add(user)

    def get(
            self, url_name=None, params=None,
            status_code=None, client=APIClient()):
        """
            custom get request to also assert status code of the
            recieved response

            :url: the endpoint to be called
            :params: dictionary of url parameters
            :status_code: status code expected from the response
            :client: client instance used in the test call
            :return: the data returned by the response
        """

        response = client.get(
            reverse(url_name, kwargs=params), format="json")
        self.assertEqual(
            response.status_code, status_code)
        return response.data

    def post(
            self, url_name=None, params=None, data=None,
            status_code=None, client=APIClient()):
        """
            custom post request to also assert status code of the
            recieved response

            :url: the endpoint to be called
            :params: dictionary of url parameters
            :data: dictionary of form data
            :status_code: status code expected from the response
            :client: client instance used in the test call
            :return: the data returned by the response
        """

        response = client.post(
            reverse(url_name, kwargs=params), data, format="json")
        self.assertEqual(
            response.status_code, status_code)
        return response.data

    def put(
            self, url_name=None, params=None, data=None,
            status_code=None, client=APIClient()):
        """
            custom get request to also assert status code of the
            recieved response

            :url: the endpoint to be called
            :params: dictionary of url parameters
            :data: dictionary of form data
            :status_code: status code expected from the response
            :client: client instance used in the test call
            :return: the data returned by the response
        """

        response = client.put(
            reverse(url_name, kwargs=params), data, format="json")
        self.assertEqual(
            response.status_code, status_code)
        return response.data

    def delete(
            self, url_name=None, params=None,
            status_code=None, client=APIClient()):
        """
            custom delete request to also assert status code of the
            recieved response

            :url: the endpoint to be called
            :params: dictionary of url parameters
            :status_code: status code expected from the response
            :client: client instance used in the test call
            :return: the data returned by the response
        """

        response = client.delete(
            reverse(url_name, kwargs=params), format="json")
        self.assertEqual(
            response.status_code, status_code)
        return response.data

    def setUp(self):
        """Define the test client and other test variables."""

        self.create_groups()

        # create application users with different rights
        # fellow
        self.fellow_user = User.objects.create(
            username="Fellow",
            google_id=1)
        self.add_to_group('Fellow', self.fellow_user)

        self.fellow_user_two = User.objects.create(
            username="Fellow2",
            google_id=2)
        self.add_to_group('Fellow', self.fellow_user_two)

        # fellow occupant
        self.fellow_user_occupant = User.objects.create(
            username="FellowOccupant",
            google_id=3)
        self.add_to_group('FellowOccupant', self.fellow_user_occupant)

        # PNC
        self.pnc_user = User.objects.create(
            username="PNC",
            google_id=4)
        self.add_to_group('PNC', self.pnc_user)

        # facilities admin
        self.admin_user = User.objects.create(
            username="FacilitiesAdmin",
            google_id=5)
        self.add_to_group('FacilitiesAdmin', self.admin_user)

        # finance
        self.finance_user = User.objects.create(
            username="Finance",
            google_id=6)
        self.add_to_group('Finance', self.finance_user)

        # Initialize client and force it to use authentication
        client = APIClient()
        client.force_authenticate(user=self.admin_user)

        # Since user model instance is not serializable, use its Id/PK
        self.space_data = {'space_name': 'St C'}
        self.space_data_two = {'space_name': 'West House'}

        self.space_response = client.post(
            reverse('create-accomodation-space'),
            self.space_data,
            format="json")

        self.space_response_two = client.post(
            reverse('create-accomodation-space'),
            self.space_data_two,
            format="json")

        self.room_data = {'room_name': 'F1', 'capacity': 4}
        self.room_data_two = {'room_name': 'F2', 'capacity': 4}

        self.room_response = client.post(
            reverse(
                'create-accomodation-room',
                kwargs={'space_id': self.space_response.data["id"]}),
            self.room_data,
            format="json")

        self.room_response_two = client.post(
            reverse(
                'create-accomodation-room',
                kwargs={'space_id': self.space_response.data["id"]}),
            self.room_data_two,
            format="json")

        self.occupant_data = {
            'user': self.fellow_user.id, 'entry_date': '2018-01-02'}
        self.occupant_data_two = {
            'user': self.fellow_user_two.id, 'entry_date': '2018-01-02'}

        self.occupant_response = client.post(
            reverse(
                'create-room-occupant',
                kwargs={'room_id': self.room_response.data["id"]}),
            self.occupant_data,
            format="json")

        self.occupant_response_two = client.post(
            reverse(
                'create-room-occupant',
                kwargs={'room_id': self.room_response.data["id"]}),
            self.occupant_data_two,
            format="json")
