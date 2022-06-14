from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import Todoserializers


# Create your views here.
class Todoviewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = Todoserializers
