from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Employer
from .serializers import EmployerSerializer


# Create your views here.
class EmployerListCreateView(generics.CreateAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Employer.objects.filter(user=user)
    
    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Employer.objects.filter(user=user)