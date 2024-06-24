from rest_framework import serializers

from .models import Project, Task, Comment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_field = ['owner', 'created_at']
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['project']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_field = ['owner', 'created_at']