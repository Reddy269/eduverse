from django.shortcuts import render,redirect
from django.http import HttpResponse
from catalog.models import InstructorProfile








def homepage(request,username):
    username = username
    if not InstructorProfile.objects.filter(username=username).exists():
        #call for onboarding
        # this view will deal with onboarding : will gwt the request data and combine
        # it with get_profile from
        return redirect(f"/catalog/onboarding/{username}")




    #

    return render(request,'catalog/homepage.html',{'username':username})

