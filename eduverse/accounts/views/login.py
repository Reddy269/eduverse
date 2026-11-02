from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.interactors.application_specific import LoginUserInteractor
from accounts.adapters.hash import PasswordHasher
from accounts.adapters.store import StoreValidation
from accounts.interactors.dtos import RequestLoginUserDTO
from accounts.interactors.exceptions import UsernameDoesNotExistError, PasswordDoesNotMatchUsernameError
from accounts.interactors.core import GetUserInteractor

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        usertype = request.POST.get("usertype")
        try:
            login_request = RequestLoginUserDTO(email_or_username=username, password=password,usertype=usertype)
        except ValueError as e:
            message = str(e)
            return HttpResponse(message,status=400)
        store_validation = StoreValidation()
        password_validation = PasswordHasher()
        try:
            LoginUserInteractor(store_validation, password_validation).login(login_request)

        except UsernameDoesNotExistError as e:
            return HttpResponse("Username does not exist",status=404)
        except PasswordDoesNotMatchUsernameError as e:
            return HttpResponse("Password does not match",status=404)
        if usertype == "instructor":
            user = GetUserInteractor()
            id = user.get_user_id()
            return redirect('catalog/')







    return render(request, 'accounts/login/login.html')