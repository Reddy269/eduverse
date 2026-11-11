from django.shortcuts import render, redirect
from django.http import Http404 , HttpResponse
from accounts.interactors.application_specific import RegisterEmailInteractor
from accounts.interactors.core import IsEmailRegisteredInteractor
from accounts.adapters.store import StoreValidation
from accounts.interactors.dtos import UserType , RequestRegisterUserDTO
from accounts.interactors.exceptions import InvalidInputError


Types = {"student", "instructor"}

def registerpage(request, usertype: str):
    template = "accounts/register/register.html"
    if usertype not in Types:
        raise Http404("Unknown registration type")

    if request.method == "POST":
        step = request.POST.get("step")

        if step == 'email':
            email = request.POST.get("email", "")
            store_validation = StoreValidation()
            email_check = IsEmailRegisteredInteractor(store_validation)
            register_email = RegisterEmailInteractor(email_check)
            try:
                register_email(email,user_type = UserType(usertype))
            except InvalidInputError as e:
                return render(request,"accounts/register/register.html", {"step": "email", "error": e.message, "email": email})
            return render(request, "accounts/register/register.html", {"step": "details", "email": email})

        elif step == 'details':
            email = request.POST.get("email", "")
            dob = request.POST.get("dob", "")
            name = request.POST.get("name", "")
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            confirm_password = request.POST.get("confirm_password", "")

            context = {
                "step": "details",
                "email": email,
                "dob": dob,
                "name": name,
                "username": username,
                "error": "passwords do not match"
            }

            if password != confirm_password:
                return render(request, "accounts/register/register.html",context)

            try:
                request_register = RequestRegisterUserDTO(user_type = usertype, email=email,name=name,dob=dob,username=username,password=password)
            except InvalidInputError as e:
                context["error"] = e.message
                return render(request,"accounts/register/register.html" ,context)

            return HttpResponse(f'details of registration :\n'
                                f'\n'
                                f'email: {email}\n'
                                f'dob: {dob}\n'
                                f'name: {name}\n'
                                f'username: {username}\n'
                                f'password: {password}\n'
                                f'confirm_password: {confirm_password}\n',
                                content_type="text/plain"
                                )






    if request.method == "GET":
        if usertype == "student":
            role_label = {"role_label" : "a student"}
        else :
            role_label = {"role_label" : "an instructor"}
        return render(request, template ,role_label )



'''
role	hidden input {{ role|default:'student' }}	string	always
role_label	page title {{ role_label|default:"a student" }}	string	always
step	{% if step == "details" %}	string	"details" for step 2, otherwise leave out or "email"
email	value="{{ email }}", plus readonly if present (step 2)	string	arriving at step 2, or when re-showing it after an error
name	{{ name }} (step 2)	string	only when re-rendering step 2 after an error
dob	{{ dob }} (step 2)	string like "2000-01-31"	only when re-rendering step 2 after an error
username	{{ username }} (step 2)	string	only when re-rendering step 2 after an error
error	popup data-server-error	string	only when something fails


@dataclass
class RequestRegisterUserDTO:
    user_type: UserType

    email: str
    name: str
    dob: date

    username: Optional[str] = None
    password: Optional[str] = None

    # checks if data is valid
    def __post_init__(self):
        try:
            self.user_type = UserType(self.user_type.strip().lower())
        except (ValueError, AttributeError):
            raise InvalidUserTypeError("invalid user type")

        if not self.name.strip():
            raise InvalidInputError("name cannot be empty")

        if not self.email.strip():
            raise InvalidInputError("email cannot be empty")

        # datetime is a subclass of date, so reject it explicitly
        if not isinstance(self.dob, date) or isinstance(self.dob, datetime):
            raise InvalidInputError("invalid date format")

        if self.dob > date.today():
            raise InvalidInputError("date of birth cannot be in the future")
'''
