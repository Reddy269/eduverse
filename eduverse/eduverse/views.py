from django.shortcuts import render
from catalog.models import Test , InstructorProfile
from django.http import HttpResponse

def homepage(request):
    return render(request, 'home.html')

def uploadtest(request):

    if request.method == 'POST':
        f = request.FILES['file']
        Test.objects.create(file=f)
        return HttpResponse('success')

    return render(request, 'upload_test.html')

def gettest(request):
    content = InstructorProfile.objects.first()
    return render(request, "get_test.html", {"content": content})

