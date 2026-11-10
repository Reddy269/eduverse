from django.shortcuts import render, redirect
from django.http import Http404 , HttpResponse

Types = {"student", "instructor"}

def registerpage(request, usertype: str):
    template = "accounts/register/register.html"
    if usertype not in Types:
        raise Http404("Unknown registration type")

    if request.method == "POST":
        pass


    if request.method == "GET":
        if usertype == "student":
            role_label = {"role_label" : "a student"}
        else :
            role_label = {"role_label" : "an instructor"}
        return render(request, template ,role_label )
