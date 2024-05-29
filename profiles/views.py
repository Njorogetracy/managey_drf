from django.db.models import Count
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Profile
from .serializers import ProfileSerializer
from managey_drf.permissions import IsOWnerorReadOnly

class ProfileList(generics.ListAPIView):
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
    permission_classes = [IsOWnerorReadOnly]
    queryset = Profile.objects.annotate(
        tasks_count = Count (
            'owner__task', distinct=True
        )
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['owner__task']
    search_fields = ['owner__username']
    serializer_class = ProfileSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
