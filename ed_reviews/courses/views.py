# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import generics

from . import models
from . import serializers

class ListCreateCourse(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class ListCreateReview(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    # this gets the queryset (mulitple items), overriding default to use course_pk to get correct filter
    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

    # override, this runs when an obj is created by the view.
    def perform_create(self, serializer):
        course = get_object_or_404(
            models.Course, pk=self.kwargs.get('course_pk'))
        serializer.save(course=course)

class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    # gets 1 item
    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            course_id=self.kwargs.get('course_pk'),
            pk=self.kwargs.get('pk')
        )