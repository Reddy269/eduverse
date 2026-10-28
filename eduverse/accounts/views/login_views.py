from django.shortcuts import render
import json
from django.http import JsonResponse
from accounts.storages import StudentStorage




def loginpage(request):
    if request.method == "GET":
        return render(request, "accounts/login/login.html")
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)

        if not isinstance(data, dict):
            return JsonResponse({"error": "Invalid request body."}, status=400)

        if StudentStorage.is_user_registered(data.get("email")):

            return JsonResponse(
                {"message" :"user not there"},
                status=201,
            )
        else:
            return JsonResponse(
                {"message":"login success"},
                status=201,
            )
