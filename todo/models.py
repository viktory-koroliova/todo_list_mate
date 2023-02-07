from django.db import models


class Tag(models.Model):
    name = models.CharField


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(to=Tag)

    class Meta:
        ordering = [
            "is_done",
            "-datetime"
        ]
