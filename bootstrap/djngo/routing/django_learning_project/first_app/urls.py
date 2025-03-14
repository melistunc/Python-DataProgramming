from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index"), #google.com/first_app/

       path("<int:num1>", views.course_number_view, name="coursenumberview"), #google.com/first_app/10

    path("<str:item>/", views.course, name="course"),#ile dışarıdan kullanıcı parametre girebilir.(str:item) google.com/first_app/python/
    
    path("<int:num1>/<int:num2>/", views.multiply_view, name="multiply"), #google.com/first_app/5/4/

 
]