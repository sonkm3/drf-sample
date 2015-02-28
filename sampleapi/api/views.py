from django.shortcuts import render

# Create your views here.

# 静的にpythonのdictをjsonとして返すAPI
from rest_framework.response import Response
from rest_framework import viewsets

class TempViewSet(viewsets.ViewSet):
    def list(self, request):
        data = {}
        data['single-int'] = 1
        data['list'] = [1,2,3]
        data['dict'] = {'key1': 'val1','key2': 'val2',}
        return Response(data)


# DBのモデルを読み書きするシンプルなAPI
from rest_framework import filters
from rest_framework import mixins
from api.models import SimpleReadWrite
from api.serializers import SimpleReadWriteSerializer

class SimpleReadWriteViewSet(viewsets.ModelViewSet):
    serializer_class = SimpleReadWriteSerializer
    model = SimpleReadWrite
    queryset = SimpleReadWrite.objects.all()


# ForeignKeyでのリレーション
from api.models import Item, ImageStore
from api.serializers import ItemSerializer, ImageStoreSerializer

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    model = Item
    queryset = Item.objects.all()


class ImageStoreViewSet(viewsets.ModelViewSet):
    serializer_class = ImageStoreSerializer
    model = ImageStore
    queryset = ImageStore.objects.all()

