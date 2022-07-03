from .models import Blogpost
from rest_framework import serializers


class BlogpostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogpost
        fields = ['url', 'title', 'author', 'content', 'tags', 'created_time', 'updated_time', 'place']
