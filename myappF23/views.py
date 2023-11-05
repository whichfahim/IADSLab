from rest_framework import status
from .models import Category, Course, AppUser, Instructor
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import CategorySerializer, AppUserSerializer

# def index(request):
#     category_list = Category.objects.all().order_by('id')[:10]
#     response = HttpResponse()
#     heading1 = '<h1>' + 'List of categories: ' + '</h1>'
#     response.write(heading1)
#     for category in category_list:
#         para = '<p>'+ str(category) + '</p>'
#         response.write(para)
#
#     course_list = Course.objects.all().order_by('-price')
#     heading2 = '<h2>' + 'List of courses by price: ' + '</h2>'
#     response.write(heading2)
#     for course in course_list:
#         para = '<p>'+ str(course) + '</p>'
#         response.write(para)
#     return response
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


def index(request):
    category_list = Category.objects.all().order_by('id')[:10]
    return render(request, 'myappF23/index0.html', {'category_list': category_list})

# def about(request):
#     response = HttpResponse()
#     heading = '<h1>' + 'This is a Distance Education Website! Search our Categories to find all available Courses.' + '</h1>'
#     response.write(heading)
#     return response

def about(request):
    return render(request, 'myappF23/about0.html')

# def detail(request, category_no):
#     response = HttpResponse()
#
#     if Course.objects.filter(categories_id=category_no).exists():
#         # at least one object satisfying query exists
#         course_list = Course.objects.filter(categories_id=category_no)
#         category = Category.objects.get(id=1)
#         heading1 = '<h1>' + 'List of courses with category: ' + str(category) + '</h1>'
#         response.write(heading1)
#
#         for course in course_list:
#             list = '<li>' + str(course) + '</li>'
#             response.write(list)
#     else:
#         # no object satisfying query exists
#         product = get_object_or_404(Course, categories_id=category_no)
#         return product
#     return response

def detail(request, category_no):
    category_name = str(Category.objects.get(id=category_no))
    course_list = Course.objects.filter(categories_id=category_no)
    context = {category_name:[]}
    for i in course_list:
        # course = {2: "two"}
        context[category_name].append(str(i))

    return render(request, 'myappF23/detail0.html',{'context': context})

