from django.db import models
from accounts.models import User


class Photo(models.Model):
    image = models.ImageField()
    details = models.CharField(max_length=50)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    favourite = models.ForeignKey(
        User, related_name="favourite", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.details


class Comment(models.Model):
    photo = models.ForeignKey(
        Photo, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    photo = models.ForeignKey(
        Photo, on_delete=models.CASCADE, related_name="rating")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
