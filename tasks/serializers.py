from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    comments_count = serializers.ReadOnlyField()
    assigned_users = UserSerializer(many=True) 

    def validate_attachment(self, value):
        if value.content_type not in ['image/jpeg', 'image/png', 'image/gif']:
            raise serializers.ValidationError('Only JPEG, PNG, and GIF images allowed')
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError('Image size is larger than 2mb!')
        if value.image.width > 2048:
            raise serializers.ValidationError('Image width is larger than 2048px!')
        if value.image.height > 2048:
            raise serializers.ValidationError('Image height is larger than 2048px!')
        return value

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
            'due_date',
            'comments_count'
        ]
