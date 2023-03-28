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
    patients = serializers.SerializerMethodField()

    class Meta:
        fields = ('email', 'first_name', 'id', 'patients')
        model = NewUser

    def get_patients(self, obj):
        patient_query = Patient.objects.filter(supervisor = obj.id)
        serializer = PatientSerializer(patient_query, many=True)

        return serializer.data