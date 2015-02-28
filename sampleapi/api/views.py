from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework import viewsets

class TempViewSet(viewsets.ViewSet):
    def list(self, request):
        data = {}
        data['single-int'] = 1
        data['list'] = [1,2,3]
        data['dict'] = {'key1': 'val1','key2': 'val2',}
        return Response(data)


