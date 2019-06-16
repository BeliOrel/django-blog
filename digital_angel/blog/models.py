from django.db import models
from django.utils import timezone
from django.urls import reverse
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

    # this method tells how to calculate the canonical URL for an object
    # [important if you use class-based views and you are dealing with pk]
    # this method returns a string that can be used to refer to
    # the object over HTTP
    # Here is used to 'redirect' to post-detail view when successfuly
    # creating a new post.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
