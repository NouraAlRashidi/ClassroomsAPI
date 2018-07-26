from rest_framework import serializers
from classes.models import Classroom
from django.contrib.auth.models import User


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id','subject', 'year', 'teacher',]


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name','subject', 'year', 'teacher',]


    
class ClassroomCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'year', 'teacher']

