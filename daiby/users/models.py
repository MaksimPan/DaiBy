from django.db import models
import uuid
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    nickname = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True) # (upload_to='profiles/', default='profiles/user-default.png')
    social_network = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.nickname)
    
    class Meta:
        ordering = ['created']

class Need(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    need_image = models.ImageField(null=True, blank=True) # (upload_to='profiles/', default='profiles/user-default.png')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
