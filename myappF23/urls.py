from django.urls import path
from myappF23 import views
from django.urls import path

app_name = 'myappF23'

urlpatterns = [
    path('', views.about, name='about'),
    path('addAppUser/', views.addAppUser, name='addAppUser'),
    path('viewAppUser/', views.viewAppUser, name='viewAppUser'),
    #path('category/delete/<int:category_no>/', views.deleteCategory, name ='deleteCategory'),
    #path('category/update/<int:category_no>/', views.updateCategory, name ='updateCategory'),
    path('instructor/instructorProfile/',views.instructorProfile, name='instructorProfile'),
    path('instructor/getInstructor/<int:ins_no>/',views.getInstructor, name='getInstructor'),
]