from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import TodoSerializer
from todo.models import Todo

# Create your views here.

class TodoList(generics.ListAPIView):
# ListAPIView requires two mandatory attributes, serializer_class and
# queryset.
# We specify TodoSerializer which we have earlier implemented
    serializer_class = TodoSerializer
    def get_queryset(self):
       user = self.request.user
       return Todo.objects.filter(user=user).order_by('-created')


class TodoListCreate(generics.ListCreateAPIView):
# ListCreateAPIView requires two mandatory attributes, serializer_class and
# queryset.
# We specify TodoSerializer which we have earlier implemented
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')


    def perform_create(self, serializer):
        #serializer holds a django model
        serializer.save(user=self.request.user)

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAdminUser]


    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
        

