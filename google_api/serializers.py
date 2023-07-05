from rest_framework import serializers

class EventSerializer(serializers.Serializer):
    summary = serializers.CharField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
