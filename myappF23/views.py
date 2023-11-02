from django.http import HttpResponse
from .models import Category, Course, Student, Instructor
from django.shortcuts import get_object_or_404
from django.shortcuts import render



def index(request):
    category_list = Category.objects.all().order_by('id')[:10]
    return render(request, 'myappF23/index.html', {'category_list': category_list})


def about(request):
    course = Course.objects.filter(id=1)
    context = {'Title':str(course)}
    context.update({'Students':[]})
    students = Course.objects.get()
    for i in students:
        context['Students'].append(str(i))

    return render(request, 'myappF23/about.html',context=context)


def detail(request, category_no):
    category_name = str(Category.objects.get(id=category_no))
    course_list = Course.objects.filter(categories_id=category_no)
    context = {category_name:[]}
    for i in course_list:
        # course = {2: "two"}
        context[category_name].append(str(i))

    return render(request, 'myappF23/detail.html',{'context': context})

def instructor(request, instructor_id):
    # instructor_name = str(Instructor.objects.get(id=instructor_id))
    course_list = Course.objects.filter(instructor_id=instructor_id)
    students = Student.objects.filter(instructors=instructor_id)
    context = {'Course':[]}
    students = Student.objects.all()
    for i in students:
        context['Students'].append(str(i))
        # context.update({'Status': i.status})
    return  render(request,'myappF23/instructor0.html',{'context':context})