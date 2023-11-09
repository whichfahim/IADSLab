from rest_framework import status
from .models import Category, Course, AppUser, Instructor
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *

@api_view(['PUT','POST'])
def addAppUser(request):
    if request.method == 'PUT':
        # Assuming request.data contains the necessary fields
        user_data = request.data

        # Creating a new User instance and saving it
        appuser = AppUser(
            name=user_data.get('name'),
            email=user_data.get('email'),
            age=user_data.get('age'),
            gender=user_data.get('gender'),
            contact_no=user_data.get('phone'),  # Assuming the field name is 'phone' in the request
            country=user_data.get('country')
        )
        appuser.save()

        return Response({'message': 'Data updated successfully'})

    return Response({'message': 'Invalid request'})

@api_view(['GET'])
def viewAppUser(request):
    appuser = AppUser.objects.all()
    serializer = AppUserSerializer(data=appuser, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateCategory(request, category_no):
    try:
        category = Category.objects.get(id=category_no)
    except Category.DoesNotExist:
        return Response({"message": "Category does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(data=category, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteCategory(request, category_no):
    try:
        category = Category.objects.get(id=category_no)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def instructorProfile(request):
    if request.method == 'POST':
        insData= request.data
        instructor = Instructor(
        first_name=insData.get('first_name'),
        last_name=insData.get('last_name'),
        bio=insData.get('bio'),
        country=insData.get('country'),
        language=insData.get('language')
    )
        instructor.save()
        return Response({"message": "Instructor profile created successfully"})
    else:
        instructor = Instructor.objects.all()
        serializer = InstructorSerializer(data=instructor, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getInstructor(request, ins_no):
    try:
        instructor = Instructor.objects.get(id=ins_no)
    except Instructor.DoesNotExist:
        return Response({"message": "Instructor does not exist"}, status=status.HTTP_404_NOT_FOUND)
    serializer = InstructorSerializer(data=instructor, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def about(request):
    return render(request, 'myappF23/about0.html')


