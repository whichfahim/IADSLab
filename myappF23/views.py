from django.shortcuts import render, get_object_or_404
# Import necessary classes
from django.http import HttpResponse
from .models import Category, Course, Student, Instructor

# Create your views here.
def index(request):
    category_list = Category.objects.all().order_by('id')[:10]
    response = HttpResponse()
    heading1 = '<h1>' + 'List of categories: ' + '</h1>'
    response.write(heading1)
    for category in category_list:
        para = '<p>'+ str(category) + '</p>'
        response.write(para)

    course_list = Course.objects.all().order_by('-price')
    heading2 = '<h2>' + 'List of courses by price: ' + '</h2>'
    response.write(heading2)
    for course in course_list:
        para = '<p>'+ str(course) + '</p>'
        response.write(para)
    return response

def about(request):
    response = HttpResponse()
    heading = '<h1>' + 'This is a Distance Education Website! Search our Categories to find all available Courses.' + '</h1>'
    response.write(heading)
    return response

def detail(request, category_no):
    # Get the category based on the category_no or return a 404 error if it doesn't exist
    category = get_object_or_404(Category, pk=category_no)

    response = HttpResponse()
    heading = '<h1' + 'This is the details page' + '</h1>'
    response.write(heading)
    # Get a list of courses for the specified category
    courses = Course.objects.filter(categories_id=category_no)

    for i in courses:
        course = "<li>"+str(i)+"</li>"
        response.write(course)

    return response

