from rest_framework import serializers

# 
from api.models import SimpleReadWrite
class SimpleReadWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleReadWrite

