from rest_framework import serializers
from .models import *



class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitlistForm
        fields = '__all__'