from django.test import TestCase

import datetime
from django.core.urlresolvers import reverse
from .models import CustomUser


class UsersTests(TestCase):

    def test_empty(self):

        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'users not found')

    def test_add_user(self):

        data = {
            'username': 'john81',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john81@gmail.com',
            'date_of_birth': '1989-05-16'
        }

        self.client.post(reverse('users:new'), data)

        self.assertEqual(CustomUser.objects.count(), 1)
        user = CustomUser.objects.first()
        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])
        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.date_of_birth, datetime.date(1989, 5, 16))

    def test_add_user_exists(self):

        data = {
            'username': 'john81',
            'date_of_birth': '1989-05-16'
        }

        response = self.client.post(reverse('users:new'), data)
        self.assertEqual(CustomUser.objects.count(), 1)

        response = self.client.post(reverse('users:new'), data)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertContains(response, 'A user with that username already exists.')
