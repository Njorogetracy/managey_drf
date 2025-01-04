from rest_framework import serializers
from .models import Profile
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'due_date', 'priority', 'state']


class ProfileSerializer(serializers.ModelSerializer):
    """
   A class for a ProfileSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    tasks_count = serializers.ReadOnlyField()
    tasks = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_tasks(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            tasks = Task.objects.filter(
                assigned_users=obj.owner, owner=request.user)
            return TaskSerializer(tasks, many=True).data
        return []

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'profile_id',
            'name', 'bio', 'image', 'is_owner', 'tasks_count', 'tasks',
        ]
