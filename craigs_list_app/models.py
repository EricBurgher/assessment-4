from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Categories(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"Category {self.name}"

class Posts(models.Model):
    content = models.TextField()
    category = ForeignKey(Categories, related_name="content", on_delete=models.CASCADE)
    creator = ForeignKey(User, related_name="content", on_delete=models.CASCADE)

    def __str__(self):
        return f"Post: {self.content} has been posted to {self.name}."
