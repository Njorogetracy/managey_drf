from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from managey_drf.permissions import IsOWnerorReadOnly
from .models import Comments
from .serializers import CommentsSerializer, CommentsDetailSerializer, CommentsUpdateSerializer

class CommentsList(generics.ListCreateAPIView):
    """
    A class to create and list the comments of the logged in user on a task
    """
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comments.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task', 'owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class to handle update and delete of comments on a task
    """
    permission_classes = [IsOWnerorReadOnly]
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CommentsUpdateSerializer
        return CommentsSerializer