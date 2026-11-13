from django.shortcuts import render,redirect
from django.http import HttpResponse
from catalog.models import Instructor








def homepage(request,user_id):
    user_id = user_id
    if not Instructor.objects.filter(id = user_id).exists():
        #call for onboarding
        # this view will deal with onboarding : will gwt the request data and combine
        # it with get_profile from
        return redirect(f"/catalog/onboarding/{user_id}")


    return HttpResponse(f"onboarding done for {user_id}")

