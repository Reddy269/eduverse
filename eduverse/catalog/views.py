from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def default(request):
    return HttpResponse('default')

def homepage(request,id):
    id = int(id)
    return render(request,'instructor/homepage.html')
