from rest_framework import serializers
from .models import images


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = images
        fields = ["img_url"]
