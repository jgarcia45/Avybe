from django.shortcuts import render
from rest_framework import viewsets
from .serializers import userProfileSerializer
from .models import userProfile

# Create your views here.
class userProfileView(viewsets.ModelViewSet):
    serializer_class = userProfileSerializer
    queryset = userProfile.objects.all()