# from django.contrib.sites import requests
from django.http import HttpResponse
from .models import Category, Course, Student, Instructor
from django.shortcuts import get_object_or_404
from django.shortcuts import render
import requests


def index(request):
    data = {}
    data["crypto_data"] = get_crypto_data()
    return render(request, "myappF23/index.html", context=data)


# return the data received from api as json object
def get_crypto_data():
    # api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
    api_url = "http://api.coinlayer.com/live?access_key=cc193be204150f270335cb8652f14683"
    try:
        data = requests.get(api_url).json()

    except Exception as e:
        print(e)
        data = dict()
    rates = data['rates']
    return rates



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