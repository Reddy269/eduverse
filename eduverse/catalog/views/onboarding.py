from django.shortcuts import render,redirect
from django.http import HttpResponse
from catalog.models import Instructor,Category
from catalog.interactors.application_specific.instructor import OnboardInstructorInteractor
from catalog.interactors.dtos import RequestOnboardInstructorDTO
from gateways.accounts_catalog_gateway import InstructorProfile
from catalog.adapters.storages import InstructorStorage
from django.http import HttpResponseRedirect





def onboarding(request,user_id):
    user_id = user_id

    instructor_profile = InstructorProfile()  # gateway implementation
    instructor_storage = InstructorStorage()  # storage implementation

    # the interactor that deals with 1) getting data from accounts and 2)storing it into a model
    onboard_instructor_interactor = OnboardInstructorInteractor(storage=instructor_storage,
                                                                gateway=instructor_profile)
    # the rturned profile_details
    profile_details = onboard_instructor_interactor.get_profile(user_id)


    if request.method == "POST":

        request_onboard = RequestOnboardInstructorDTO(id = profile_details.user_id,
                                                      username = profile_details.username,
                                                      display_name = profile_details.name,
                                                      email = profile_details.email,
                                                      dob = profile_details.dob,
                                                      bio = None,
                                                      category = None,
                                                      dp_picture = None,
                                                      )

        '''
        @dataclass
class RequestOnboardInstructorDTO:
    id: str
    username: str
    display_name: str
    email: str
    dob: date
    bio: str
    category: str
    dp_picture: Optional[UploadedFile]


    def __post_init__(self):
        pass
        
        user_id: str
    name: str
    email: str
    username: str
    dob: date
        
        '''


        # data from onboard page
        display_name = request.POST.get("displayname","" ).strip()  or request_onboard.display_name
        bio = request.POST.get("bio", "").strip()  # "" means fill later
        category_id = request.POST.get("expertise")  # one value per chosen category
        profile_pic = request.FILES.get("profile_pic")  # None if not uploaded

        # now we have overall data : accounts + onboard page

        # update request DTO for storing
        request_onboard.display_name = display_name
        request_onboard.bio = bio
        request_onboard.category = category_id
        request_onboard.dp_picture = profile_pic

        # save to db
        onboard_instructor_interactor.save_profile(request_onboard)


        # redirect to homepage

        return HttpResponseRedirect(f"/catalog/{user_id}")

    category = []
    for c in Category.objects.filter(parent_id__isnull=True):
        category.append(c)
    return render(request, "instructor/onboard_instructor.html", {
        "default_display_name": profile_details.name,
        "categories": category,  # objects or dicts with .id and .name
    })

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

