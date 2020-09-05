from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    # This class also in charge of validating the types of input data
    name = serializers.CharField(max_length = 10)
