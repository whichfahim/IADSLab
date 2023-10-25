from django.http import HttpResponseNotFound
from django.http import HttpResponse
from .models import Category, Course, Student, Instructor
from django.shortcuts import get_object_or_404

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
    response = HttpResponse()

    if Course.objects.filter(categories_id=category_no).exists():
        # at least one object satisfying query exists
        course_list = Course.objects.filter(categories_id=category_no)
        category = Category.objects.get(id=1)
        heading1 = '<h1>' + 'List of courses with category: ' + str(category) + '</h1>'
        response.write(heading1)

        for course in course_list:
            list = '<li>' + str(course) + '</li>'
            response.write(list)
    else:
        # no object satisfying query exists
        # response.write()
        # return HttpResponseNotFound("This Category number does not exist.")
        product = get_object_or_404(Course, categories_id=category_no)
        return product
    return response

