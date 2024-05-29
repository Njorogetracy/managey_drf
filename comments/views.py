from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from managey_drf.permissions import IsOWnerorReadOnly
from .models import Comments
from .serializers import CommentsSerializer, CommentsDetailSerializer

class CommentsList(generics.ListCreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comments.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task', 'owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOWnerorReadOnly]
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()