from django.urls import path
from myappF23 import views
from django.urls import path

app_name = 'myappF23'

urlpatterns = [
    path(r'', views.index, name='index'),
    # path("/about", views.about, name='about')
    path('addAppUser/', views.addAppUser, name='addAppUser'),
    #path('addUser/', views.about, name='about'),
    path('viewAppUser/', views.viewAppUser, name='viewAppUser'),
    #path('category/delete/<int:category_no>/', views.deleteCategory, name ='deleteCategory'),
    #path('category/update/<int:category_no>/', views.updateCategory, name ='updateCategory'),
    path('category/<int:category_no>/', views.detail, name='detail'),
]