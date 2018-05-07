from rest_framework import serializers
from . import models


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    lessons = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='slug')

    class Meta:
        model = models.Module
        fields = '__all__'


# class ModuleLessonSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = models.ModuleLesson
#        fields = '__all__'

class WorkshopSerializer(serializers.ModelSerializer):
    modules = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='slug')

    lessons = LessonSerializer(many=True)

    class Meta:
        model = models.Workshop
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    workshops = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='slug')

    class Meta:
        model = models.Track
        fields = '__all__'


# class TrackModuleSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = models.TrackModule
#        fields = '__all__'