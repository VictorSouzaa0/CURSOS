from django.shortcuts import get_object_or_404
from rest_framework import generics

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from .models import Course,Assessment
from .serializer import CourseSerializer,AssessmentSerializer
from .permissions import IsSuperUser

from rest_framework import permissions

"""
API V1

!!! Realizando CRUD com rest_framework-generics
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


!!! Realizando CRUD com rest_framework-iewSets
"""

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Adicionando um decorators pois viewsets quando cria os endpoints não reconhece os relacionamentos
# É necessário criar um decorator para realizar esse relacionamento


    @action(detail=True,methods=['get'])
    def assessments(self,resquest,pk=None):
#Adicionando paginação no decorators pois o django.filter só reconhece as tabelas raiz
        self.pagination_class.page_size = 1
        assessments = Assessment.objects.filter(course_id=pk)
        page = self.paginate_queryset(assessments)

        if page is not None:
            serializer = AssessmentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AssessmentSerializer(assessments,many=True)
        return Response(serializer.data)

"""

!! - ViewsSets.modelViewSet : Te permite ter acesso a todos os métodos

class AssesstsViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
"""


#Mixins permite que você insira de forma manual quais CRUD's você deseja fazer
class AssesstsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):

    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer