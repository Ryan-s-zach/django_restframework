# serializers.py
from rest_framework import serializers
from .models import TouristDestination

class TouristDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristDestination
        fields = ['id', 'name', 'description', 'latitude', 'longitude', 'image', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']  # Make created_at and updated_at read-only

    def create(self, validated_data):
        """
        Create and return a new TouristDestination instance, given the validated data.
        """
        return TouristDestination.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing TouristDestination instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
