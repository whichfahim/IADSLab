from rest_framework import serializers

from myappF23.models import Category, Course, Student, Instructor


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'