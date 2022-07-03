from .models import Blogpost
from django.shortcuts import get_object_or_404
from .serializers import BlogpostSerializer
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

class BlogpostViewSet(viewsets.ModelViewSet):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [DjangoModelPermissions]
        return [permission() for permission in permission_classes]
