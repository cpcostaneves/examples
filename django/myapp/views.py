#from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework import viewsets

from .serializers import PersonSerializer
from .models import Person


# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ExplicitPersonViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving data.
    """
    def list(self, request):
        queryset = Person.objects.all()
        serializer = ExplicitPersonSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ExplicitPersonSerializer(user)
        return Response(serializer.data)