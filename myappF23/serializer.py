from rest_framework import serializers

from myappF23.models import Category, User, Student, Instructor


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields = '__all__'