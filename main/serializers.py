from rest_framework import serializers
from .models import VideoUrl


class SongsSerializers(serializers.ModelSerializer):
    class Meta:
        model = VideoUrl
        fields = '__all__'
