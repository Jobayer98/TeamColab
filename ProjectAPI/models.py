from django.db import models
from UserAPI.models import CustomUser as User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=550, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name


class ProjectMember(models.Model):
    ROLE_CHOICES = {
        "member": "Member",
        "admin": "Admin"
    }
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, default="admin")
    
    def __str__(self) -> str:
        return f"{self.project.name} | {self.user.username}"
    

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in-progress", "In Progress"),
        ("done", "Done")
    ]
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High")
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=550, blank=True, null=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default="low")
    assigned_to = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.title
    
    
class Comments(models.Model):
    content = models.TextField(max_length=350)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.content[:10]