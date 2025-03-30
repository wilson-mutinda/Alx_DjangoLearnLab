from django.shortcuts import render

from .serializers import NotificationSerializer
from .models import Notification
from rest_framework import generics, permissions

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user, is_read=False)
