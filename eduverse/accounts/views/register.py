from django.shortcuts import render, redirect
from django.http import Http404 , HttpResponse

REGISTER_TEMPLATES = {
    "student": "accounts/register/student_register.html",
    "instructor": "accounts/register/instructor_register.html",
}

def registerpage(request, usertype: str):
    template = REGISTER_TEMPLATES.get(usertype)
    if template is None:
        raise Http404("Unknown registration type")

    if request.method == "GET":
        return render(request, template)
