from django.shortcuts import render
from django.http import JsonResponse
import json


from accounts.interactors.dtos import RequestRegisterUserDTO
from accounts.interactors.register_user_interactor import RegisterUserInteractor
from accounts.interactors.core.create_user_interactor import CreateUserInteractor
from accounts.storages import StudentStorage
from accounts.adapters.password_hasher import PasswordHasher
from accounts.interactors.exceptions import EmailAlreadyExistsError
from accounts.interactors.dtos import RequestRegisterUserDTO
from accounts.adapters.send_signal import SendSignalAdapter
from accounts.storages.student_storage import StudentStorage


def student_registerpage(request):
    if request.method == 'GET':
        return render(request, 'accounts/register/student_register.html')

    elif request.method=="POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)

        if not isinstance(data, dict):
            return JsonResponse({"error": "Invalid request body."}, status=400)

        if data.get("password") != data.get("confirm_password"):
            return JsonResponse({"error": "Passwords do not match."}, status=400)

        try:
            dto = RequestRegisterUserDTO(
                name=data.get("name", ""),
                email=data.get("email", ""),
                password=data.get("password", ""),
                UserType="student",  # fixed by this view, not read from the body
            )
            storage = StudentStorage()
            hasher = PasswordHasher()
            create_user = CreateUserInteractor(storage,hasher)
            signal = SendSignalAdapter()
            register_user = RegisterUserInteractor(dto,signal,create_user)
            user = register_user.execute()
        except EmailAlreadyExistsError as e:
            return JsonResponse({"error": str(e)}, status=409)

    return JsonResponse(
        {"name": user.name, "email": user.email, "usertype": user.usertype},
        status=201,
    )


