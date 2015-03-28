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


# ForeignKeyでのリレーション
from api.models import Item, ImageStore
from api.serializers import ItemSerializer, ImageStoreSerializer

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    model = Item


class ImageStoreViewSet(viewsets.ModelViewSet):
    serializer_class = ImageStoreSerializer
    model = ImageStore


# モデルのフィールドとシリアライザのフィールドの数が違う場合
from api.models import FieldSample
from api.serializers import FieldSampleFullSerializer, FieldSampleMinimumSerializer

# defaultが設定されていてもnullableではないフィールドは入力が必須
class FieldSampleFullViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSampleFullSerializer
    model = FieldSample

# シリアライザにnullableでないフィールドが含まれていない場合、そのフィールドはデフォルト値が設定される
class FieldSampleMinimumViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSampleMinimumSerializer
    model = FieldSample


from api.serializers import NestedItemSerializer
# ForeignKeyでのリレーション(mixin使う)
class MixinedItemViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = ItemSerializer
    model = Item

    def list(self, request):
        queryset = Item.objects.all()
        serializer = NestedItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Item.objects.get(pk=pk)
        serializer = NestedItemSerializer(queryset)
        return Response(serializer.data)

    # def update(self, request):
    #     return super(MixinedItemViewSet, self).update()
    # 
    # def partial_update(self, request):
    #     return super(MixinedItemViewSet, self).partial_update()

# ForeignKeyでのリレーション(mixin使わない)
# GETとPOST/PUT/DELETEでシリアライザーを使い分けることでGET時にはreadonly fieldでネストさせつつ、POST/PUT時にはリレーションのPK渡すことができる
class ModelViewSetItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    model = Item

    def list(self, request):
        queryset = Item.objects.all()
        serializer = NestedItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Item.objects.get(pk=pk)
        serializer = NestedItemSerializer(queryset)
        return Response(serializer.data)


from api.serializers import ItemSerializerWithSource
# 他のモデルを参照しているフィールドを展開する際にシリアライザを指定して展開する
# PrimaryKeyRelatedFieldで参照するよりも細かく指定できるが書き込みには使えない
class ItemSerializerWithSourceViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    model = Item

    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemSerializerWithSource(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Item.objects.get(pk=pk)
        serializer = ItemSerializerWithSource(queryset)
        return Response(serializer.data)

from api.serializers import SimpleReadWriteSerializerWithSerializerMethodField
# SerializerMethodFieldを使ってモデルに無いフィールドを動的に生成する
class SerializerMethodFieldViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SimpleReadWriteSerializerWithSerializerMethodField
    model = Item

