from space.tests.base import BaseTestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status

class OccupantTestCases(BaseTestCase):

    def test_occupant_can_be_created(self):
        self.assertEqual(
            self.occupant_response.status_code, status.HTTP_201_CREATED)

    def test_occupants_can_be_listed(self):

        client = APIClient()
        client.force_authenticate(user=self.admin_user)

        data = self.get(
            'view-room-occupant',
            {
                "room_id": self.occupant_response.data["id"]
            },
            status_code=status.HTTP_200_OK,
            client=client)
        self.assertEqual(len(data), 2)

    def test_can_retrieve_single_occupant(self):

        client = APIClient()
        client.force_authenticate(user=self.admin_user)

        data = self.get(
            'retrieve-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status.HTTP_200_OK, client)

        self.assertEqual(data["id"], self.occupant_response.data["id"])

    def test_occupant_can_be_updated(self):

        client = APIClient()
        client.force_authenticate(user=self.admin_user)

        data = self.put(
            'update-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={
                'user': self.fellow_user.id,
                "entry_date": '2020-04-05'
            },
            status_code=status.HTTP_200_OK, client=client)

        self.assertEqual(data["entry_date"], '2020-04-05')

    def test_occupant_can_be_deleted(self):

        client = APIClient()
        client.force_authenticate(user=self.admin_user)

        self.delete(
            'delete-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            }, status.HTTP_204_NO_CONTENT,
            client=client)

    def test_occupant_cant_be_seen_by_unauthenticated_users(self):

        self.get(
            'view-room-occupant',
            {
                "room_id": self.occupant_response.data["id"]
            }, status_code=status.HTTP_401_UNAUTHORIZED)

    def test_cant_retrieve_single_occupant_by_unauthenticated_user(self):

        self.get(
            'retrieve-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_401_UNAUTHORIZED)

    def test_occupant_cant_be_created_by_unauthenticated_users(self):

        self.post(
            'create-room-occupant',
            {
                "room_id": self.room_response.data["id"],
            },
            data={
                'user': "ABC",
                "entry_date": '2020-03-07'
            },
            status_code=status.HTTP_401_UNAUTHORIZED)

    def test_occupant_cant_be_updated_by_unauthenticated_user(self):

        self.put(
            'update-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={'space_name': 'St ABC'},
            status_code=status.HTTP_401_UNAUTHORIZED)

    def test_occupant_cant_be_deleted_by_unauthenticated_user(self):

        self.delete(
            'delete-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_401_UNAUTHORIZED)

    def test_occupant_cant_be_created_by_finance_users(self):

        client = APIClient()
        client.force_authenticate(user=self.finance_user)

        self.post(
            'create-room-occupant',
            {
                "room_id": self.room_response.data["id"],
            },
            data={
                'user': "ABC",
                "entry_date": '2020-03-07'
            },
            status_code=status.HTTP_403_FORBIDDEN,
            client=client)

    def test_occupant_cant_be_updated_by_finance_user(self):

        client = APIClient()
        client.force_authenticate(user=self.finance_user)
        self.put(
            'update-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={'space_name': 'St ABC'},
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_occupant_cant_be_deleted_by_finance_user(self):

        client = APIClient()
        client.force_authenticate(user=self.finance_user)
        self.delete(
            'delete-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_occupant_cant_be_created_by_pnc_users(self):

        client = APIClient()
        client.force_authenticate(user=self.pnc_user)

        self.post(
            'create-room-occupant',
            {
                "room_id": self.room_response.data["id"],
            },
            data={
                'user': "ABC",
                "entry_date": '2020-03-07'
            },
            status_code=status.HTTP_403_FORBIDDEN,
            client=client)

    def test_occupant_cant_be_updated_by_pnc_user(self):

        client = APIClient()
        client.force_authenticate(user=self.pnc_user)
        self.put(
            'update-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={'space_name': 'St ABC'},
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_occupant_cant_be_deleted_by_pnc_user(self):

        client = APIClient()
        client.force_authenticate(user=self.pnc_user)
        self.delete(
            'delete-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_occupant_cant_be_created_by_fellow_users(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user)

        self.post(
            'create-room-occupant',
            {
                "room_id": self.room_response.data["id"],
            },
            data={
                'user': "ABC",
                "entry_date": '2020-03-07'
            },
            status_code=status.HTTP_403_FORBIDDEN,
            client=client)

    def test_occupant_cant_be_updated_by_fellow_user(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user)
        self.put(
            'update-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={'space_name': 'St ABC'},
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_occupant_cant_be_deleted_by_fellow_user(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user)
        self.delete(
            'delete-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_occupant_cant_be_created_by_fellow_occupant_users(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user_occupant)

        self.post(
            'create-room-occupant',
            {
                "room_id": self.room_response.data["id"],
            },
            data={
                'user': "ABC",
                "entry_date": '2020-03-07'
            },
            status_code=status.HTTP_403_FORBIDDEN,
            client=client)

    def test_occupant_cant_be_updated_by_fellow_occupant_user(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user_occupant)
        self.put(
            'update-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={'space_name': 'St ABC'},
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_occupant_cant_be_deleted_by_fellow_occupant_user(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user_occupant)
        self.delete(
            'delete-room-occupant',
            {
                "occupant_id": self.occupant_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_403_FORBIDDEN, client=client)
