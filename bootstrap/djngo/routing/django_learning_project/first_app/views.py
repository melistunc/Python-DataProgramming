from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

#reverse isimden item bulmaktır.

course_dictionary = {
    "python" : "Python Course Page",
    "java" : "Java Course Page",
    "swift": "Swift course Page",
    "kotlin": "Kotlin course Page"}

def index(request):
    return HttpResponse("This is first Django project, first index")


def course(request, item):
    try:
        course = course_dictionary[item]
        return HttpResponse(course)
    except:
        return HttpResponseNotFound("Not found please another course!")
        #raise Http404("Not found please another course!")    

    #return HttpResponse(course_dictionary.get(item,"not found!")) #girilen değer views'te yoksa not found yazsın. varsa iten olarak girilisin.

def multiply_view(request, num1, num2):
        return HttpResponse(f"{num1} * {num2} = {num1 * num2}") #dışarıdan girilen iki sayının çarpımı.

def course_number_view(request, num1): #google.com + 10 yaparsa
    course_list = list(course_dictionary.keys( ))
    try:
      course = course_list[num1]        
      page_to_go = reverse("course", args=[course]) #parametre olarak urls'de yazdığımız path isimlerini yazıyoruz. index isminden hangi py yoluna gidileceğini bulur. 
      return HttpResponseRedirect(page_to_go)

    except:
         return HttpResponseNotFound("Not found please another course!")

    
    #return HttpResponseRedirect(f"/first_app/{course}") #redirect yönlendirme isteğidir. yazdığımızı belirttiğimiz sayfaya yönlendirir. 10 yazınca swift'e gitmesi gibi. 0 yazınca python, 1 yazınca java vs diye isteklere yönlendirir.
    
    
    #if num1 == 10:
        #return HttpResponseRedirect("/first_app/swift") #google.com/firts_app/10 yazdığımızda swift'e gidecek.
    #else:
        #return HttpResponseRedirect("Not found!Please look for another course!") #10 dışında bir şey yazarsak bu mesaj verilsin.