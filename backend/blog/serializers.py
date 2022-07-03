from .models import Blogpost
from rest_framework import serializers
from accounts.serializers import UserSerializer


class BlogpostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Blogpost
        fields = [
            "url",
            "title",
            "author",
            "content",
            "tags",
            "created_time",
            "updated_time",
            "place",
        ]
