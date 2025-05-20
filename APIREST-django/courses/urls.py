from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import (
               CourseAPiView,
               AssessmentAPiView,
               CoursesAPiView,
               AssessmentsAPiView,
               CourseViewSet,
               AssesstsViewSet,
                    )



router = SimpleRouter()
router.register('courses',CourseViewSet)
router.register('assessments',AssesstsViewSet)

urlpatterns = [
     path('courses/',CoursesAPiView.as_view(),name='courses'),
     path('courses/<int:pk>',CourseAPiView.as_view(),name="course"),
     path('courses/<int:course_pk>/assessments/',AssessmentsAPiView.as_view(),name='courses asssessments'),
     path('courses/<int:course_pk>/assessments/<int:assessment_pk>/',AssessmentsAPiView.as_view(),name='courses asssessments'),

     path('assessment/',AssessmentsAPiView.as_view(),name="assessments"),
     path('assessment/<int:pk>',AssessmentAPiView.as_view(),name='assessment'),
     


]
