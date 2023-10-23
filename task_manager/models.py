from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    efforts = models.IntegerField(default=2)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
