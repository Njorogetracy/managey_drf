from django.contrib.auth.models import User
from .models import Task
from rest_framework import status
from rest_framework.test import APITestCase


class TaskViewTests(APITestCase):
    def setUp(self):
        self.july = User.objects.create_user(
            username='july', password='password1')

    def test_loggedin_user_can_create_task(self):
        """
        Tests that authenticated user can create task
        """
        self.client.login(username='july', password='password1')
        response = self.client.post(
            '/tasks/', {'title': 'task title', 'assigned_users': self.july.id})
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
        Task.objects.create(
            owner=july, assigned_users_id=july.id, title='task title')
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TaskDetailTests(APITestCase):
    def setUp(self):
        july = User.objects.create_user(username='july', password='password1')
        juni = User.objects.create_user(username='juni', password='password23')
        Task.objects.create(
            owner=july, title='task title', description='julys task content')
        Task.objects.create(
            owner=juni, title='task 2 title', description='junis task content')

    def test_user_can_retrieve_existing_task(self):
        """
        Test if users can retrieve task
        """

        response = self.client.get('/tasks/1/')
        print(response)
        self.assertEqual(response.data['title'], 'task title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_nonexistent_task(self):
        """
        Test if users can retrieve task which does not exist
        """

        response = self.client.get('/tasks/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_task(self):
        """
        Test that users can update tasks that they own
        """
        self.client.login(username='july', password='password1')
        response = self.client.put('/tasks/1/', {'title': 'new task title'})
        post = Task.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'new task title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_task_they_dont_own(self):
        self.client.login(username='juni', password='password23')
        response = self.client.put('/tasks/1/', {'title': 'new task title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_delete_own_task(self):
        """
        Test that users can delete their tasks
        """
        self.client.login(username='july', password='password1')
        response = self.client.delete('/tasks/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_other_users_task(self):
        self.client.login(username='july', password='password1')
        response = self.client.put('/tasks/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        """
        runs after every test method to ensure \
        each test starts with a clean slate
        """
        Task.objects.all().delete()
        User.objects.all().delete()
