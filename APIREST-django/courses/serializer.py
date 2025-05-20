from rest_framework import serializers

from .models import Course,Assessment


class AssessmentSerializer(serializers.ModelSerializer):
  
    class Meta:
        extra_kwargs ={
            'email': {'write_only': True}
        }
        model = Assessment
        fields = ('id',
                  'course',
                  'email',
                  'comments',
                  'assessment',
                  'creates',
                  'active'
                  )


class CourseSerializer(serializers.ModelSerializer):
    """
    Nested Relationship
    assessments = AssessmentSerializer(many=True,read_only=True)
    """

    #HyperLinked Related Field
    assessments = serializers.HyperlinkedRelatedField(
                                                many=True, 
                                                read_only=True, 
                                                view_name="asssessment-detail")
    class Meta:
        model = Course
        fields = (
                  'id',
                  'title',
                  'url',
                  'creates',
                  'active',
                'assessments',
                )