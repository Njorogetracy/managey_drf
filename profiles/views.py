from django.db.models import Count
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Profile
from .serializers import ProfileSerializer
from managey_drf.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    A class to list all profiles
    """
    serializer_class = ProfileSerializer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    ordering_fields = ['owner__task', 'created_at']
    search_fields = ['owner__username']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Profile.objects.annotate(
            tasks_count=Count('owner__task', distinct=True)
        ).order_by('-created_at')

        if self.request.user.is_superuser:
            return queryset

        if self.request.user.is_authenticated:
            return queryset

        return queryset 
    


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class for a profile detail.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        tasks_count=Count(
            'owner__task', distinct=True
        )
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['owner__task']
    search_fields = ['owner__username']

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Handles deletion of a profile.
        """
        return self.destroy(request, *args, **kwargs)