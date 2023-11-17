from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Category, Course, Student, Instructor, Order
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from myappF23.forms import OrderForm, InterestForm


# def index(request):
#     category_list = Category.objects.all().order_by("id")[:10]
#     return render(request, "myappF23/index.html", {"category_list": category_list})
def index(request):
    category_list = Category.objects.all().order_by("id")[:10]
    course_list = Course.objects.all().order_by("-price")[:5]
    order_list = Order.objects.all().order_by("-order_date")[:10]
    ins_list = Instructor.objects.all()[:5]

    return render(
        request,
        "myappF23/index.html",
        {
            "course_list": course_list,
            "category_list": category_list,
            "order_list": order_list,
            "ins_list": ins_list,
        },
    )

def about(request):
    # course = Course.objects.filter(id=1)
    # context = {'Title':str(course)}
    # context.update({'Students':[]})
    # students = Course.objects.get()
    # for i in students:
    #     context['Students'].append(str(i))

    return render(request, "myappF23/about.html")


# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("myappF23:index"))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details.")
    else:
        return render(request, "myappF23/login.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(("myappF23:index")))


def detail(request, category_no):
    category_name = str(Category.objects.get(id=category_no))
    course_list = Course.objects.filter(categories_id=category_no)
    context = {category_name: []}
    for i in course_list:
        # course = {2: "two"}
        context[category_name].append(str(i))

    return render(request, "myappF23/detail.html", {"context": context})


def instructor(request, instructor_id):
    # instructor_name = str(Instructor.objects.get(id=instructor_id))
    course_list = Course.objects.filter(instructor_id=instructor_id)
    students = Student.objects.filter(instructors=instructor_id)
    context = {"Course": []}
    students = Student.objects.all()
    for i in students:
        context["Students"].append(str(i))
        # context.update({'Status': i.status})
    return render(request, "myappF23/instructor0.html", {"context": context})


def courses(request):
    courselist = Course.objects.all().order_by("id")
    return render(request, "myappF23/courses.html", {"courselist": courselist})

def place_order(request):
    msg = ''
    courlist = Course.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            msg = 'Your course has been ordered successfully.'
        else:
            msg = 'You exceeded the number of levels for this course.'
            return render(request, 'myappF23/order_response.html', {'msg': msg})
    else:
        form = OrderForm()
    return render(request, 'myappF23/placeorder.html', {'form':form, 'msg':msg, 'courlist':courlist})
