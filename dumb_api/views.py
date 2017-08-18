from django.shortcuts import render
from rest_framework import viewsets
from .models import DumbTable
from .serializer import DumbSerializer


class DumbViewSet(viewsets.ModelViewSet):
    queryset = DumbTable.objects.all()
    serializer_class = DumbSerializer
