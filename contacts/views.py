from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Contact
from .serializers import ContactSerializer

# Create your views here.
class ContactList(ListCreateAPIView):

    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        print('\n'*10)
        print(request)
        print('\n'*10)
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
    


class ContactDetail(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = "pk"

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

