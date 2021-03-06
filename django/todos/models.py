from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
