from rest_framework import serializers

# 
from api.models import SimpleReadWrite
class SimpleReadWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleReadWrite


from api.models import Item, ImageStore



class ImageStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageStore
        fields = ('id', 'image',)
        read_only_fields = ('id',)


class ItemSerializer(serializers.ModelSerializer):
    image = serializers.PrimaryKeyRelatedField(many=False, required=False)
    class Meta:
        model = Item
        fields = ('id', 'name', 'image')
        read_only_fields = ('id',)
        depth = 1



from api.models import FieldSample
class FieldSampleFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldSample
        fields = ('required_field', 'required_field_with_default', 'nullable_field', 'nullable_field_with_default')


class FieldSampleMinimumSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldSample
        fields = ('required_field',)



