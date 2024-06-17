from django.db.models import Count
from django.http import Http404
from rest_framework import generics, status, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Task
from .serializers import TaskSerializer
from managey_drf.permissions import IsOwnerOrReadOnly

class TaskList(generics.ListCreateAPIView):
    """
    A class to create and list the tasks of the logged in user
    """
    queryset = Task.objects.annotate(
        comments_count = Count(
            'comments', distinct=True
        )
    ).order_by('-created_at')
    serializer_class = TaskSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['owner__username', 'priority', 'state']
    ordering_fields = ['comments_count']
    filterset_fields = ['priority','state','assigned_users']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class to handle update and deleting of the tasks
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

