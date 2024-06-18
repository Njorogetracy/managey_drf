from django.db.models import Count
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Profile
from .serializers import ProfileSerializer
from managey_drf.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListAPIView):
    """
    A class to list all profiles
    """
    queryset = Profile.objects.annotate(
        tasks_count = Count (
            'owner__task', distinct=True
        )
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    ordering_fields = ['owner__task']
    search_fields = ['owner__username']

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    A class for a profile detail.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        tasks_count = Count (
            'owner__task', distinct=True
        )
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['owner__task']
    search_fields = ['owner__username']

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
