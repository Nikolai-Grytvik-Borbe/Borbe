from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer
from .models import User
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]

