from django.db import models


class AppUser(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=90)
    contact_no=models.CharField(max_length=10)
    country=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    STUDENT_STATUS_CHOICES=[
        ('ER','Enrolled'),
        ('SP','Suspended'),
        ('GD','Graduated')
    ]

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254, unique=True)
    date_of_birth=models.DateField()
    status=models.CharField(max_length=10,choices=STUDENT_STATUS_CHOICES,default='ER')

    def __str__(self):
        return f"{self.first_name} {self.last_name} Email:{self.email}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True, related_name='courses_teaching')
    categories=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    students=models.ManyToManyField(Student,blank=True)
    start_date=models.DateField()
    end_date=models.DateField()
    price=models.DecimalField(max_digits=10,decimal_places=2)


    #level choices in Course

    COURSE_LEVEL_CHOICES=[
        ('BE','Beginner'),
        ('IN', 'Intermediate'),
        ('AD','Advanced'),
    ]

    level=models.CharField(max_length=15,choices=COURSE_LEVEL_CHOICES,default='BE')

    def __str__(self):
        return self.title


class Instructor(models.Model):
    user_name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    bio=models.TextField()
    country=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    email=models.CharField(max_length=50)


    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}"


class Order(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    ORDER_STATUS_CHOICES = [
        (0, 'Order Confirmed'),
        (1, 'Order Cancelled')
    ]
    order_status = models.IntegerField(choices=ORDER_STATUS_CHOICES,default='1')
    order_date = models.DateField()
