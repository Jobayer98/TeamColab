from rest_framework import serializers

from .models import Project, ProjectMember, Task, Comment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_field = ['owner', 'created_at']