from django.db import models
from UserAPI.models import CustomUser as User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=550, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
