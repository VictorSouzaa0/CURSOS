from django.shortcuts import get_object_or_404
from rest_framework import generics

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Course,Assessment
from .serializer import CourseSerializer,AssessmentSerializer


"""
API V1
"""
class CourseAPiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer 

class CoursesAPiView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer 



class AssessmentsAPiView(generics.ListCreateAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()

class AssessmentAPiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

    def get_object(self):
        if self.kwargs.get('course_pk'):
            return get_object_or_404(self.get_queryset(),course_id=self.kwargs.get('course_pk'),
                                                        pk=self.kwargs.get('assessment_pk'))
        return get_object_or_404(self.get_queryset(),pk=self.kwargs.get('assessment_pk'))
    
"""
API V2
"""

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

    @action(detail=True,methods=['get'])
    def assessments(self,resquest,pk=None):
        course = self.get_object()
        serializer = AssessmentSerializer(course.assessment.all(),many=True)
        return Response(serializer.data)


class AssesstsViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer