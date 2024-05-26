from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from managey_drf.permissions import IsOWnerorReadOnly

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOWnerorReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
