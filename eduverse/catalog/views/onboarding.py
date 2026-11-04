from django.shortcuts import render,redirect
from django.http import HttpResponse
from catalog.models import InstructorProfile,Category
from catalog.interactors.application_specific.instructor import OnboardInstructorInteractor
from catalog.interactors.dtos import RequestInstructorProfileDTO
from catalog.interactors.dtos import RequestOnboardInstructorDTO
from gateways.accounts_catalog_gateway import InstructorProfile
from catalog.adapters.storages import InstructorStorage





def onboarding(request,username):
    username = username

    if request.method == "POST":
        instructor_profile = InstructorProfile() # gateway implementation
        instructor_storage = InstructorStorage() # storage implementation

        #the interactor that deals with 1) getting data from accounts and 2)storing it into a model
        onboard_instructor_interactor = OnboardInstructorInteractor(storage=instructor_storage,
                                                                    gateway=instructor_profile)
        #DTO for requesting details from accounts
        request_profile = RequestInstructorProfileDTO(username=username)
        #the rturned profile_details
        profile_details = onboard_instructor_interactor.get_profile(request_profile)


        # data from onboard page
        display_name = request.POST.get("displayname","" ).strip()  or profile_details.display_name
        bio = request.POST.get("bio", "").strip()  # "" means fill later
        category_id = request.POST.get("expertise")  # one value per chosen category
        profile_pic = request.FILES.get("profile_pic")  # None if not uploaded

        # now we have overall data : accounts + onboard page

        # request DTO for storing
        request_onboard = RequestOnboardInstructorDTO(
                                username=profile_details.username,
                                email = profile_details.email,
                                display_name = display_name,
                                dob = profile_details.dob,
                                bio = bio,
                                dp_file=profile_pic,
                                category = category_id,

                         )

        onboard_instructor_interactor.save_profile(request_onboard)
        '''
        class RequestOnboardInstructorDTO:
            username: str
    display_name: str
    email: str
    dob: str
    bio: str
    category: str
    dp_file: 


    def __post_init__(self):
        pass
        onboard_instructor_interactor.execute(
            OnboardInstructorRequest(
                user_id=request.user.id,
                display_name=display_name or None,
                bio=bio or None,
                category_id=category_id,
                profile_pic=profile_pic,
            )
        )
        '''
        return HttpResponse(f"instructor_dashboard , {display_name} , {bio} , {category_id} , {profile_pic}, --> {profile_details}")
    category = []
    for c in Category.objects.filter(parent_id__isnull=True):
        category.append(c)
    return render(request, "instructor/onboard_instructor.html", {
        "default_display_name": username,
        "categories": category,  # objects or dicts with .id and .name
    })