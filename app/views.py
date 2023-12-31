from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from datetime import datetime
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import *
from .serializers import MenuItemSerializer, MenuSerializer, BookingSerializer, NotificationSerializer


class MenuView(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [AllowAny,]

class MenuItemView(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    permission_classes = [AllowAny,]

class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [AllowAny,]

    def create(self, request):
        request.data["date"] = datetime.strptime(request.data["date"], '%a, %d %b %Y %H:%M:%S GMT')
        serializer = self.serializer_class(
            data=request.data
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, status="booking")
            status_no = 'new' if self.request.user.role.name == 2 else 'read'
            Notification.objects.create(booking=serializer.instance, status=status_no)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class NotificationView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [AllowAny,]
    pagination_class = None

class RetriveNotificationView(RetrieveUpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [AllowAny,]

    def update(self, request, *args, **kwargs):
        object = self.get_object()
        object.status = 'read'
        object.save()
        return Response(self.serializer_class(object).data)
