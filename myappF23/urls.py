from django.urls import path
from . import views
from django.urls import path

app_name = 'myappF23'

urlpatterns = [
    path(r'', views.index, name='index'),
    # path("/about", views.about, name='about')
    path('about/', views.about, name='about'),
    path('category/<int:category_no>/', views.detail, name='detail'),
    path('instructor/<int:instructor_id>/', views.instructor, name='instructor'),
    path('courses/',views.courses, name='courses'),
    path('orders/',views.place_order)
]