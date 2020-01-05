from rest_framework import serializers

class SampleSerializer(serializers.Serializer):
    """Serializes our name field for testing our API view"""
    name = serializers.CharField(max_length=10)