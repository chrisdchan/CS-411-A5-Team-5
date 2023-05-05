from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewUser
        exclude = ('user_permissions',)



class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"




class NestedSerializer(serializers.ModelSerializer):
    meetings = serializers.SerializerMethodField()

    class Meta:
        fields = ('email', 'first_name', 'id', 'meetings')
        model = NewUser

    def get_meetings(self, obj):
        audio_query = Audio.objects.filter(supervisor = obj.id)
        serializer = AudioSerializer(audio_query, many=True)

        return serializer.data