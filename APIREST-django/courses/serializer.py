from rest_framework import serializers

from .models import Course,Assessment


class AssessmentSerializer(serializers.ModelSerializer):
  
    class Meta:
        extra_kwargs ={
            'email': {'write_only': True}
        }
        model = Assessment
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'