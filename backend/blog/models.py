from django.db import models
from accounts.models import User

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    tags = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    place = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.title} | {self.created_time}"

class Comment(models.Model):
    text = models.TextField()
    edited = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blogpost = models.ForeignKey(Blogpost(), on_delete=models.CASCADE)


