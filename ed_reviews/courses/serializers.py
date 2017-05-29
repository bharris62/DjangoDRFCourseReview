from rest_framework import serializers
from . import models

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created_at'
        )
        model = models.Review

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        reviews = serializers.PrimaryKeyRelatedField(many=True,
                                                      read_only=True, )

        fields = (
            'id',
            'title',
            'url',
            'reviews',
        )
        model = models.Course