from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# User:Post = 1:n

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # if User is deleted then we're gonna delete their posts too
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title # title is displayed when asking for object
