from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.interactors.application_specific import LoginUserInteractor
from accounts.adapters.hash import PasswordHasher
from accounts.adapters.store import StoreValidation, UserStorage
from accounts.interactors.dtos import RequestLoginUserDTO , UserType
from accounts.interactors.core import GetUserIdInteractor , GetPasswordInteractor
from accounts.adapters.store import storage_validation

from accounts.interactors.exceptions import InvalidInputError



def loginpage(request):
    if request.method == 'POST':
        identifier = request.POST.get("username")
        password = request.POST.get("password")
        usertype = request.POST.get("usertype")

        try:
            login_request = RequestLoginUserDTO(identifier = identifier, password = password, user_type = usertype)
        except ValueError as e:
            message = str(e)
            return render(request, "accounts/login/login.html", {"error": message}, status=401)




        '''
        storage_validation:StorageValidationInterface,
                 password_validation:PasswordHasherInterface,
                 get_password:GetPasswordInteractor,
        '''

        store_validation = StoreValidation()
        password_validation = PasswordHasher()
        user_storage = UserStorage()
        get_password = GetPasswordInteractor(user_storage)
        login_user = LoginUserInteractor(storage_validation=store_validation, password_validation=password_validation,
                                         get_password=get_password,storage=user_storage)
        try:
            user_id = login_user.login(login_request)
        except InvalidInputError as e:
            return render(request, "accounts/login/login.html", {"error": e.message}, status=402)

        except ValueError as e:
            return HttpResponse("Password does not match",status=404)

        if user_id == False:
            return render(request, "accounts/login/login.html", {"error": f"password did not match identifier {login}"}, status=401)

        if login_request.user_type == UserType.INSTRUCTOR :
            return redirect(f"/catalog/{user_id}/")

        return HttpResponse(f"Login successful : {user_id}")








    return render(request, 'accounts/login/login.html')