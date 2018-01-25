from space.tests.base import BaseTestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status

class RoomTestCases(BaseTestCase):

    def test_room_can_be_created(self):
        self.assertEqual(
            self.space_response.status_code, status.HTTP_201_CREATED)

    def test_rooms_can_be_listed(self):

        client = APIClient()
        client.force_authenticate(user=self.admin_user)

        data = self.get(
            'view-accomodation-room',
            {
                "space_id": self.space_response.data["id"]
            },
            status_code=status.HTTP_200_OK,
            client=client)
        self.assertEqual(len(data), 2)

    def test_can_retrieve_single_room(self):

        client = APIClient()
        client.force_authenticate(user=self.admin_user)

        data = self.get(
            'retrieve-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status.HTTP_200_OK, client)

        self.assertEqual(data["id"], self.space_response.data["id"])

    def test_room_can_be_updated(self):

        client = APIClient()
        client.force_authenticate(user=self.admin_user)

        data = self.put(
            'update-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={
                'room_name': 'F11',
                "capacity": 2
            },
            status_code=status.HTTP_200_OK, client=client)

        self.assertEqual(data["room_name"], 'F11')
        self.assertEqual(data["capacity"], 2)

    def test_room_can_be_deleted(self):

        client = APIClient()
        client.force_authenticate(user=self.admin_user)

        self.delete(
            'delete-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            }, status.HTTP_204_NO_CONTENT,
            client=client)

    def test_room_cant_be_seen_by_unauthenticated_users(self):

        self.get(
            'view-accomodation-room',
            {
                "space_id": self.space_response.data["id"]
            }, status_code=status.HTTP_401_UNAUTHORIZED)

    def test_cant_retrieve_single_room_by_unauthenticated_user(self):

        self.get(
            'retrieve-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_401_UNAUTHORIZED)

    def test_room_cant_be_created_by_unauthenticated_users(self):

        self.post(
            'create-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
            },
            data={'space_name': "ABC"},
            status_code=status.HTTP_401_UNAUTHORIZED)

    def test_room_cant_be_updated_by_unauthenticated_user(self):

        self.put(
            'update-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={'space_name': 'St ABC'},
            status_code=status.HTTP_401_UNAUTHORIZED)

    def test_room_cant_be_deleted_by_unauthenticated_user(self):

        self.delete(
            'delete-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_401_UNAUTHORIZED)

    def test_room_cant_be_created_by_finance_users(self):

        client = APIClient()
        client.force_authenticate(user=self.finance_user)

        self.post(
            'create-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
            },
            data={
                'room_name': "ABC",
                "capacity": 4
            },
            status_code=status.HTTP_403_FORBIDDEN,
            client=client)

    def test_room_cant_be_updated_by_finance_user(self):

        client = APIClient()
        client.force_authenticate(user=self.finance_user)
        self.put(
            'update-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={'space_name': 'St ABC'},
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_room_cant_be_deleted_by_finance_user(self):

        client = APIClient()
        client.force_authenticate(user=self.finance_user)
        self.delete(
            'delete-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_room_cant_be_created_by_pnc_users(self):

        client = APIClient()
        client.force_authenticate(user=self.pnc_user)

        self.post(
            'create-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
            },
            data={
                'room_name': "ABC",
                "capacity": 4
            },
            status_code=status.HTTP_403_FORBIDDEN,
            client=client)

    def test_room_cant_be_updated_by_pnc_user(self):

        client = APIClient()
        client.force_authenticate(user=self.pnc_user)
        self.put(
            'update-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={'space_name': 'St ABC'},
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_room_cant_be_deleted_by_pnc_user(self):

        client = APIClient()
        client.force_authenticate(user=self.pnc_user)
        self.delete(
            'delete-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_room_cant_be_created_by_fellow_users(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user)

        self.post(
            'create-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
            },
            data={
                'room_name': "ABC",
                "capacity": 4
            },
            status_code=status.HTTP_403_FORBIDDEN,
            client=client)

    def test_room_cant_be_updated_by_fellow_user(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user)
        self.put(
            'update-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={'space_name': 'St ABC'},
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_room_cant_be_deleted_by_fellow_user(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user)
        self.delete(
            'delete-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_room_cant_be_created_by_fellow_occupant_users(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user_occupant)

        self.post(
            'create-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
            },
            data={
                'room_name': "ABC",
                "capacity": 4
            },
            status_code=status.HTTP_403_FORBIDDEN,
            client=client)

    def test_room_cant_be_updated_by_fellow_occupant_user(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user_occupant)
        self.put(
            'update-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            data={'space_name': 'St ABC'},
            status_code=status.HTTP_403_FORBIDDEN, client=client)

    def test_room_cant_be_deleted_by_fellow_occupant_user(self):

        client = APIClient()
        client.force_authenticate(user=self.fellow_user_occupant)
        self.delete(
            'delete-accomodation-room',
            {
                "space_id": self.space_response.data["id"],
                "room_id": self.room_response.data["id"]
            },
            status_code=status.HTTP_403_FORBIDDEN, client=client)
