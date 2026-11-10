from django.shortcuts import render, redirect
from django.http import Http404 , HttpResponse
from accounts.interactors.application_specific import RegisterEmailInteractor
from accounts.interactors.core import IsEmailRegisteredInteractor
from accounts.adapters.store import StoreValidation
from accounts.interactors.dtos import UserType
from accounts.interactors.exceptions import InvalidInputError


Types = {"student", "instructor"}

def registerpage(request, usertype: str):
    template = "accounts/register/register.html"
    if usertype not in Types:
        raise Http404("Unknown registration type")

    if request.method == "POST":
        step = request.POST.get("step")
        email = request.POST.get("email", "")

        if step == 'email':
            store_validation = StoreValidation()
            email_check = IsEmailRegisteredInteractor(store_validation)
            register_email = RegisterEmailInteractor(email_check)
            try:
                register_email(email,user_type = UserType(usertype))
            except InvalidInputError as e:
                return HttpResponse(e.message, status=400)
            return HttpResponse('email does not exist proceed to registration')





    if request.method == "GET":
        if usertype == "student":
            role_label = {"role_label" : "a student"}
        else :
            role_label = {"role_label" : "an instructor"}
        return render(request, template ,role_label )
