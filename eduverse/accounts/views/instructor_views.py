from django.shortcuts import render

def instructor_home(request, instructor_id):
    return render(request,"homepage/instructor_home.html",  {"instructor_id": instructor_id})