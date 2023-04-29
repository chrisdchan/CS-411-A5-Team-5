from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'phone', 'link']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewUser
        exclude = ('user_permissions',)

class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.SerializerMethodField
    class Meta:
        model = Resource
        fields = "__all__"

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.SerializerMethodField
    trainings = serializers.SerializerMethodField
    class Meta:
        model = Course
        fields = "__all__"

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
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