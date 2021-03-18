from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
