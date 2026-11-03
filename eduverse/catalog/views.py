from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def default(request):
    return HttpResponse('default')

def homepage(request,id):
    instructor_id = id
    return HttpResponse(f'instructor_id : {instructor_id}')
