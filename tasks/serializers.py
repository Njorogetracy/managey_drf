from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField()
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = [
            'id', 
            'is_owner',
            'profile_image',
            'profile_id',
            'owner', 
            'created_at', 
            'updated_at', 
            'title', 
            'description', 
            'attachment', 
            'overdue', 
            'assigned_users', 
            'priority', 
            'state', 
            'due_date'  
        ]
