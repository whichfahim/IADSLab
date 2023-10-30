from django.http import HttpResponse
from .models import Category, Course, Student, Instructor
from django.shortcuts import get_object_or_404
from django.shortcuts import render

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

def instructor(request, instructor_id):
    instructor_name = str(Instructor.objects.get(id=instructor_id))
    courses = Course.objects.filter(instructor_id=instructor_id)
    context = {'Instructor':instructor_name}
    context.update({'Courses': courses})
    return  render(request,'myappF23/instructor0.html',{'context':context})