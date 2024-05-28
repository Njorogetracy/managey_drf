from django.contrib.auth.models import User
from .models import Task
from rest_framework import status
from rest_framework.test import APITestCase


class TaskViewTests(APITestCase):
    def setUp(self):
       self.july = User.objects.create_user(username='july', password='password1')


    def test_loggedin_user_can_create_task(self):
        """
        Tests that authenticated user can create task
        """
        self.client.login(username='july', password='password1')
        response = self.client.post('/tasks/', {'title': 'task title', 'assigned_users': self.july.id})
        count = Task.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_loggedout_user_cant_create_task(self):
        """
        Tests that non authenticated user cannot create a task
        """

        response = self.client.post('/tasks/', {'title': 'task title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_list_tasks(self):
        """
        Test that checks for list of all tasks in the database
        """
        july = User.objects.get(username='july')
        Task.objects.create(owner=july, assigned_users_id=july.id, title='task title')
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)